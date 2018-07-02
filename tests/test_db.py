import json
from unittest import mock
import uuid

from gps_routes.db import add_way_point


def test_add_first_way_point():
    mock_route = mock.Mock()
    mock_db_session = mock.Mock(
        query=mock.Mock(
            return_value=mock.Mock(
                filter_by=mock.Mock(
                    return_value=mock.Mock(
                        first=mock.Mock(return_value=(mock_route, None)),
                    )
                )
            )
        ),
    )

    route_id = uuid.uuid4()
    latitude, longitude = 52.14, 21.00
    add_way_point(route_id, latitude, longitude, mock_db_session)

    assert mock_route.way_points == "LINESTRING(21.0 52.14, 21.0 52.14)"


def test_add_second_way_point():
    mock_route = mock.Mock()
    mock_way_points_json = json.dumps({
        "type": "LineString",
        "coordinates": [[21.0, 52.13], [21.0, 52.13]],
    })
    mock_db_session = mock.Mock(
        query=mock.Mock(
            return_value=mock.Mock(
                filter_by=mock.Mock(
                    return_value=mock.Mock(
                        first=mock.Mock(
                            return_value=(mock_route, mock_way_points_json),
                        ),
                    )
                )
            )
        ),
    )

    route_id = uuid.uuid4()
    latitude, longitude = 52.31, 13.24
    add_way_point(route_id, latitude, longitude, mock_db_session)

    assert (
        mock_route.way_points
        == "LINESTRING(21.0 52.13, 21.0 52.13, 13.24 52.31)"
    )
