from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()


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
