import uuid

from connexion import NoContent
import flask

from . import db


def create_route() -> dict:
    with db.session_scope() as db_session:
        route = db.create_route(db_session)

        return {"route_id": route.id.hex}


def add_way_point(route_id: str) -> (NoContent, int):
    route_id = uuid.UUID(route_id)
    request_body = flask.request.get_json()
    latitude, longitude = request_body["lat"], request_body["lon"]

    with db.session_scope() as db_session:
        db.add_way_point(route_id, latitude, longitude, db_session)

    return NoContent, 204


def get_length(route_id: str) -> dict:
    route_id = uuid.UUID(route_id)

    with db.session_scope() as db_session:
        return {
            "km": int(db.get_route_length(route_id, db_session) / 1000),
        }
