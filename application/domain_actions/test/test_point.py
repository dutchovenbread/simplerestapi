import json
from datetime import datetime, timedelta

import pytest

from domain_actions.point import Point  # Assuming your Point class is in a file called point.py

# Test data for parametrization
test_data = [
  (52.5200, 13.4050, 34.5, datetime(2024, 9, 26, 12, 34, 56)),
  (-33.8688, 151.2093, 10.0, datetime(2024, 8, 10, 8, 30, 0)),
  (40.7128, -74.0060, 5.2, datetime(2025, 1, 1, 0, 0, 0)),
  (35.6895, 139.6917, 40.1, datetime.utcnow() + timedelta(days=1))  # Future date with timedelta
]

@pytest.mark.parametrize("lat, lon, ele, time", test_data)
def test_point_to_dict(lat, lon, ele, time):
  """Test the to_dict method of the Point class."""
  point = Point(lat, lon, ele, time)
  point_dict = point.to_dict()

  assert point_dict['lat'] == lat
  assert point_dict['lon'] == lon
  assert point_dict['ele'] == ele
  assert point_dict['time'] == time.isoformat()

@pytest.mark.parametrize("lat, lon, ele, time", test_data)
def test_point_from_dict(lat, lon, ele, time):
  """Test the from_dict method of the Point class."""
  data = {
    'lat': lat,
    'lon': lon,
    'ele': ele,
    'time': time.isoformat()
  }

  point = Point.from_dict(data)

  assert point.lat == lat
  assert point.lon == lon
  assert point.ele == ele
  assert point.time == time

@pytest.mark.parametrize("lat, lon, ele, time", test_data)
def test_point_json_serialization(lat, lon, ele, time):
  """Test that the Point object is correctly serialized to JSON."""
  point = Point(lat, lon, ele, time)
  point_json = json.dumps(point.to_dict())

  expected_json = json.dumps({
    'lat': lat,
    'lon': lon,
    'ele': ele,
    'time': time.isoformat()
  })
  assert point_json == expected_json

@pytest.mark.parametrize("lat, lon, ele, time", test_data)
def test_point_json_deserialization(lat, lon, ele, time):
  """Test that a JSON string is correctly deserialized into a Point object."""
  point_json = json.dumps({
    'lat': lat,
    'lon': lon,
    'ele': ele,
    'time': time.isoformat()
  })

  point_dict_from_json = json.loads(point_json)
  point = Point.from_dict(point_dict_from_json)

  assert isinstance(point, Point)
  assert point.lat == lat
  assert point.lon == lon
  assert point.ele == ele
  assert point.time == time

@pytest.mark.parametrize("lat, lon, ele, time", test_data)
def test_point_to_dict_only(lat, lon, ele, time):
  """Test the serialization of a Point object to a dictionary."""
  point = Point(lat, lon, ele, time)
  point_dict = point.to_dict()

  expected_dict = {
    'lat': lat,
    'lon': lon,
    'ele': ele,
    'time': time.isoformat()
  }
  assert point_dict == expected_dict

@pytest.mark.parametrize("lat, lon, ele, time", test_data)
def test_point_from_dict_only(lat, lon, ele, time):
  """Test the deserialization of a dictionary into a Point object."""
  data = {
    'lat': lat,
    'lon': lon,
    'ele': ele,
    'time': time.isoformat()
  }

  point = Point.from_dict(data)

  assert isinstance(point, Point)
  assert point.lat == lat
  assert point.lon == lon
  assert point.ele == ele
  assert point.time == time
