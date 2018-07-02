from unittest import mock
import uuid

from gps_routes import web


@mock.patch("gps_routes.web.flask.request")
@mock.patch("gps_routes.web.db.add_way_point")
def test_add_way_point(mock_db_add_way_point, mock_request):
    route_id = uuid.uuid4()
    latitude, longitude = 52.13, 21.0
    mock_request.get_json.return_value = {"lat": latitude, "lon": longitude}

    web.add_way_point(route_id.hex)

    mock_db_add_way_point.assert_called_once_with(
        route_id, latitude, longitude, mock.ANY,
    )
