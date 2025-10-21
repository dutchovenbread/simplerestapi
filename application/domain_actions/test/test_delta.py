from datetime import datetime

import pytest

from domain_actions.point import Point
from domain_actions.delta import Delta

# Sample test cases for deltas
test_cases_delta = [
  (
    Point(38.8895, -77.0091, 34.0, datetime(2024, 7, 4, 12, 0, 0)),  # US Capitol
    Point(38.8977, -77.0365, 30.0, datetime(2024, 7, 4, 12, 0, 6)),   # White House
    1.58,  # Expected distance in miles
    -4.0,  # Expected elevation difference (34.0 - 30.0)
    (datetime(2024, 7, 4, 12, 0, 6) - datetime(2024, 7, 4, 12, 0, 0)).total_seconds()  # Expected time difference
  ),
  (
    Point(38.8895, -77.0353, 34.0, datetime(2024, 7, 4, 12, 0, 0)),  # Washington Monument (corrected)
    Point(38.889369, -77.040428, 26.0, datetime(2024, 7, 4, 12, 0, 12)),  # WWII Memorial (updated)
    0.28,  # Updated expected distance in miles (approx. direct distance)
    -8.0,  # Expected elevation difference (34.0 - 26.0)
    (datetime(2024, 7, 4, 12, 0, 12) - datetime(2024, 7, 4, 12, 0, 0)).total_seconds()  # Expected time difference
  ),
  (
    Point(38.8962258331049, -77.0494466582248, 20.0, datetime(2024, 7, 4, 12, 0, 0)),  # Pan American Health Organization Headquarters (updated)
    Point(38.8926935931272, -77.04048810096855, 22.0, datetime(2024, 7, 4, 12, 0, 24)),  # Organization of American States Headquarters (updated)
    0.54,  # Expected distance in miles (approx. direct distance)
    2.0,   # Expected elevation difference (22.0 - 20.0)
    (datetime(2024, 7, 4, 12, 0, 24) - datetime(2024, 7, 4, 12, 0, 0)).total_seconds()  # Expected time difference
  )
]

@pytest.mark.parametrize("point_a, point_b, expected_distance, expected_ele, expected_time", test_cases_delta)
def test_delta(point_a, point_b, expected_distance, expected_ele, expected_time):
  """Test that Delta correctly calculates differences between two points."""
  delta = Delta(point_a, point_b)

  assert round(delta.d_distance, 2) == round(expected_distance, 2)  # Check distance to hundredths of a mile
  assert delta.d_ele == expected_ele
  assert delta.d_time.total_seconds() == expected_time


def test_delta_initialization_with_climb():
  """Test Delta initialization with an explicit climb value."""
  point_a = Point(38.8962258331049, -77.0494466582248, 20.0, datetime(2024, 7, 4, 12, 0, 0))
  point_b = Point(38.8926935931272, -77.04048810096855, 22.0, datetime(2024, 7, 4, 12, 0, 24))
  explicit_climb = 5.0

  delta = Delta(point_a, point_b, climb=explicit_climb)

  assert delta.climb == explicit_climb
  assert delta.d_distance == pytest.approx(0.540, rel=1e-2)
  assert delta.d_ele == pytest.approx(2.0, rel=1e-1)
  assert delta.d_time.total_seconds() == pytest.approx(24.0, rel=1e-1)

def test_delta_initialization_without_climb():
  """Test Delta initialization without an explicit climb value."""
  point_a = Point(38.8962258331049, -77.0494466582248, 20.0, datetime(2024, 7, 4, 12, 0, 0))
  point_b = Point(38.8926935931272, -77.04048810096855, 22.0, datetime(2024, 7, 4, 12, 0, 24))

  delta = Delta(point_a, point_b)

  expected_climb = max(0, point_b.ele - point_a.ele)
  assert delta.climb == expected_climb
  assert delta.d_distance == pytest.approx(0.540, rel=1e-2)
  assert delta.d_ele == pytest.approx(2.0, rel=1e-1)
  assert delta.d_time.total_seconds() == pytest.approx(24.0, rel=1e-1)


def test_delta_initialization():
  """Test that Delta initializes correctly with two points."""
  point_a = Point(38.8895, -77.0091, 34.0, datetime(2024, 7, 4, 12, 0, 0))  # US Capitol
  point_b = Point(38.8977, -77.0365, 30.0, datetime(2024, 7, 4, 12, 0, 6))  # White House
  delta = Delta(point_a, point_b)
  assert round(delta.d_distance, 2) == round(1.58, 2)  # Check distance to hundredths of a mile
  assert delta.d_ele == -4.0
  assert delta.d_time.total_seconds() == (datetime(2024, 7, 4, 12, 0, 6) - datetime(2024, 7, 4, 12, 0, 0)).total_seconds()
