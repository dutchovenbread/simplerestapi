from datetime import datetime

import pytest

from domain_actions.point import Point
from domain_actions.segment import Segment
from domain_actions.activity import Activity

# Sample test data
point_a = Point(38.8895, -77.0091, 34.0, datetime(2024, 7, 4, 12, 0, 0))  # US Capitol
point_b = Point(38.8977, -77.0365, 30.0, datetime(2024, 7, 4, 12, 0, 6))  # White House
segment = Segment([point_a, point_b])

def test_activity_initialization():
  """Test the initialization of an Activity."""
  activity = Activity(name="Morning Run", date=datetime(2024, 7, 4), segments=[], a_type="Running")
  assert activity.name == "Morning Run"
  assert activity.date == datetime(2024, 7, 4)
  assert activity.segments == []
  assert activity.a_type == "Running"

def test_add_segment():
  """Test adding a segment to the Activity."""
  activity = Activity(name="Morning Run", date=datetime(2024, 7, 4), segments=[], a_type="Running")
  activity.add_segment(segment)
  assert len(activity.segments) == 1
  assert activity.segments[0] == segment

def test_activity_to_dict():
  """Test converting an Activity to a dictionary."""
  activity = Activity(name="Morning Run", date=datetime(2024, 7, 4), segments=[segment], a_type="Running")
  activity_dict = activity.to_dict()
  expected_dict = {
    'segments': [segment.to_dict()],
    'name': "Morning Run",
    'date': datetime(2024, 7, 4).isoformat(),
    'a_type': "Running"
  }
  assert activity_dict == expected_dict

def test_activity_from_dict():
  """Test creating an Activity from a dictionary."""
  activity_dict = {
    'segments': [segment.to_dict()],
    'name': "Morning Run",
    'date': datetime(2024, 7, 4).isoformat(),
    'a_type': "Running"
  }
  activity = Activity.from_dict(activity_dict)
  assert activity.name == "Morning Run"
  assert activity.date == datetime(2024, 7, 4)
  assert len(activity.segments) == 1
  assert activity.a_type == "Running"

def test_activity_total_climb():
  """Test the total climb calculation for an activity."""
  points = [
    Point(38.8962258331049, -77.0494466582248, 20.0, datetime(2024, 7, 4, 12, 0, 0)),
    Point(38.8926935931272, -77.04048810096855, 22.0, datetime(2024, 7, 4, 12, 0, 24)),
    Point(38.8895, -77.0091, 30.0, datetime(2024, 7, 4, 12, 1, 0)),
  ]
  segment = Segment(points)
  activity = Activity(name="Test Activity", date=datetime(2024, 7, 4), segments=[segment], a_type="Running")

  total_climb = activity.get_total_climb()
  expected_climb = 10.0  # Example expected climb value
  assert total_climb == pytest.approx(expected_climb, rel=1e-1)

def test_activity_splits_climb():
  """Test the climb calculation for activity splits."""
  points = [
    Point(38.8962258331049, -77.0494466582248, 20.0, datetime(2024, 7, 4, 12, 0, 0)),
    Point(38.8926935931272, -77.04048810096855, 22.0, datetime(2024, 7, 4, 12, 0, 24)),
    Point(38.8895, -77.0091, 30.0, datetime(2024, 7, 4, 12, 1, 0)),
  ]
  segment = Segment(points)
  activity = Activity(name="Test Activity", date=datetime(2024, 7, 4), segments=[segment], a_type="Running")

  splits = activity.get_splits(0.5)  # Example split length
  assert splits[0].climb == pytest.approx(2.0, rel=1e-1)
  assert splits[1].climb == pytest.approx(8.0, rel=1e-1)

# Run the tests
pytest.main()
