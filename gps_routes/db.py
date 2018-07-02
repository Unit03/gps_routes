from contextlib import contextmanager
import json
import uuid

from geoalchemy2 import Geometry, functions
from sqlalchemy import Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import UUIDType

DeclarativeBase = declarative_base()
Session = sessionmaker()


class Route(DeclarativeBase):
    __tablename__ = "routes"

    id = Column(UUIDType, primary_key=True)
    way_points = Column(Geometry(geometry_type="LINESTRING"), nullable=False)


def create_route(db_session: Session) -> Route:
    route = Route(id=uuid.uuid4())
    db_session.add(route)

    return route


def get_route(route_id: uuid.UUID, db_session: Session) -> Route:
    route = db_session.query(Route).get(route_id)

    return route


def add_way_point(
        route_id: uuid.UUID,
        latitude: float,
        longitude: float,
        db_session: Session,
) -> None:
    route, way_points = (
        db_session
        .query(Route, functions.ST_AsGeoJSON(Route.way_points))
        .filter_by(id=route_id)
        .first()
    )

    # Points use longitude, latitude order.
    if way_points is not None:
        coordinates = json.loads(way_points)["coordinates"]
    else:
        coordinates = [[longitude, latitude]]

    coordinates.append([longitude, latitude])

    coordinates_str = ', '.join(f"{lon} {lat}" for lon, lat in coordinates)
    route.way_points = f"LINESTRING({coordinates_str})"


def get_route_length(route_id: uuid.UUID, db_session: Session) -> float:
    return (
        db_session
        .query(functions.ST_Length(Route.way_points, True))
        .filter_by(id=route_id)
        .limit(1)
        .scalar()
    )


def initialize(dsn: str) -> None:
    Session.configure(bind=create_engine(dsn, pool_pre_ping=True))


@contextmanager
def session_scope(session=None, *, isolation_level=None):
    """Provide a transactional scope around a series of operations."""
    if session is None:
        session = Session()

    if isolation_level:
        session.connection(
            execution_options={"isolation_level": isolation_level},
        )

    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()
