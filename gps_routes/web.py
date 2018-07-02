import uuid

from connexion import NoContent


def create_route() -> dict:
    route_id = uuid.uuid4()

    return {"route_id": route_id.hex}


def add_way_point(route_id: str) -> (NoContent, int):
    route_id = uuid.UUID(route_id)

    return NoContent, 204


def get_length(route_id: str) -> dict:
    route_id = uuid.UUID(route_id)

    return {"km": 0}
