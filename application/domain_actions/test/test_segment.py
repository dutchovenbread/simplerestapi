from datetime import datetime

import pytest

from domain_actions.point import Point
from domain_actions.segment import Segment

# Sample test cases for points
test_cases_segment = [
  (
    [
      Point(38.8895, -77.0091, 34.0, datetime(2024, 7, 4, 12, 0, 0)),  # US Capitol
      Point(38.8936, -77.0228, 32.0, datetime(2024, 7, 4, 12, 0, 3)),
      Point(38.8977, -77.0365, 30.0, datetime(2024, 7, 4, 12, 0, 6)),   # White House
    ],
    [0.790,0.790],  # Expected distances in miles
    [-2.0,-2.0],  # Expected elevation differences (34.0 - 30.0)
    [(datetime(2024, 7, 4, 12, 0, 3)-datetime(2024, 7, 4, 12, 0, 0)).total_seconds(),(datetime(2024, 7, 4, 12, 0, 6)-datetime(2024, 7, 4, 12, 0, 3)).total_seconds()]
  ),
  (
    [
      Point(38.8895, -77.0353, 34.0, datetime(2024, 7, 4, 12, 0, 0)),  # Washington Monument (corrected)
      Point(38.889369, -77.040428, 26.0, datetime(2024, 7, 4, 12, 0, 12)),  # WWII Memorial (updated)
    ],
    [0.276],  # Expected distance in miles (approx. direct distance)
    [-8.0],  # Expected elevation difference (34.0 - 26.0)
    [(datetime(2024, 7, 4, 12, 0, 12) - datetime(2024, 7, 4, 12, 0, 0)).total_seconds()]
  ),
  (
      [
          Point(38.8962258331049, -77.0494466582248, 20.0, datetime(2024, 7, 4, 12, 0, 0)),  # Pan American Health Organization Headquarters (updated)
          Point(38.8926935931272, -77.04048810096855, 22.0, datetime(2024, 7, 4, 12, 0, 24)),  # Organization of American States Headquarters (updated)
      ],
      [0.540],  # Expected distance in miles (approx. direct distance)
      [2.0],   # Expected elevation difference (22.0 - 20.0)
      [(datetime(2024, 7, 4, 12, 0, 24) - datetime(2024, 7, 4, 12, 0, 0)).total_seconds()]  # Expected time difference
  ),
  (
    [
      Point(38.843914000, -77.108920000, 54.7, datetime(2024, 9, 27, 23, 25, 4)),
      Point(38.843914000, -77.108920000, 55.0, datetime(2024, 9, 27, 23, 25, 4)),
      Point(38.844000000, -77.108910000, 55.4, datetime(2024, 9, 27, 23, 25, 16)),
      Point(38.844086000, -77.108900000, 55.8, datetime(2024, 9, 27, 23, 25, 27)),
      Point(38.844166000, -77.108910000, 56.2, datetime(2024, 9, 27, 23, 25, 38)),
      Point(38.844254000, -77.108894000, 56.5, datetime(2024, 9, 27, 23, 25, 51)),
      Point(38.844337000, -77.108890000, 57.2, datetime(2024, 9, 27, 23, 26, 1)),
      Point(38.844420000, -77.108880000, 57.7, datetime(2024, 9, 27, 23, 26, 10)),
      Point(38.844500000, -77.108860000, 58.3, datetime(2024, 9, 27, 23, 26, 19)),
      Point(38.844580000, -77.108840000, 58.7, datetime(2024, 9, 27, 23, 26, 28)),
      Point(38.844670000, -77.108826000, 59.2, datetime(2024, 9, 27, 23, 26, 38)),
      Point(38.844753000, -77.108820000, 59.5, datetime(2024, 9, 27, 23, 26, 46)),
      Point(38.844837000, -77.108826000, 59.6, datetime(2024, 9, 27, 23, 26, 54)),
      Point(38.844925000, -77.108820000, 59.7, datetime(2024, 9, 27, 23, 27, 2)),
      Point(38.845010000, -77.108820000, 59.6, datetime(2024, 9, 27, 23, 27, 10)),
      Point(38.845093000, -77.108810000, 59.5, datetime(2024, 9, 27, 23, 27, 21)),
      Point(38.845184000, -77.108810000, 59.2, datetime(2024, 9, 27, 23, 27, 32)),
      Point(38.845270000, -77.108780000, 58.8, datetime(2024, 9, 27, 23, 27, 43)),
      Point(38.845350000, -77.108770000, 58.5, datetime(2024, 9, 27, 23, 27, 52)),
      Point(38.845436000, -77.108760000, 58.2, datetime(2024, 9, 27, 23, 28, 1)),
      Point(38.845516000, -77.108730000, 57.8, datetime(2024, 9, 27, 23, 28, 11)),
      Point(38.845562000, -77.108635000, 57.4, datetime(2024, 9, 27, 23, 28, 22)),
      Point(38.845543000, -77.108530000, 56.9, datetime(2024, 9, 27, 23, 28, 43)),
      Point(38.845497000, -77.108430000, 56.4, datetime(2024, 9, 27, 23, 28, 53)),
      Point(38.845460000, -77.108340000, 55.8, datetime(2024, 9, 27, 23, 29, 1)),
      Point(38.845417000, -77.108246000, 55.4, datetime(2024, 9, 27, 23, 29, 11)),
      Point(38.845352000, -77.108170000, 54.8, datetime(2024, 9, 27, 23, 29, 21)),
      Point(38.845284000, -77.108090000, 54.4, datetime(2024, 9, 27, 23, 29, 30)),
      Point(38.845215000, -77.108020000, 53.9, datetime(2024, 9, 27, 23, 29, 37)),
      Point(38.845158000, -77.107950000, 53.4, datetime(2024, 9, 27, 23, 29, 44)),
      Point(38.845078000, -77.107900000, 52.8, datetime(2024, 9, 27, 23, 29, 54)),
      Point(38.845005000, -77.107840000, 52.3, datetime(2024, 9, 27, 23, 30, 4)),
      Point(38.844948000, -77.107760000, 51.7, datetime(2024, 9, 27, 23, 30, 14)),
      Point(38.844868000, -77.107720000, 51.5, datetime(2024, 9, 27, 23, 30, 21)),
      Point(38.844790000, -77.107666000, 51.3, datetime(2024, 9, 27, 23, 30, 33)),
      Point(38.844727000, -77.107605000, 51.1, datetime(2024, 9, 27, 23, 30, 42)),
      Point(38.844677000, -77.107510000, 50.9, datetime(2024, 9, 27, 23, 30, 51)),
      Point(38.844610000, -77.107530000, 50.7, datetime(2024, 9, 27, 23, 31, 10))
    ],
    [
      0.0,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.006,0.005,0.006,0.006,0.006,0.006,0.005,0.006,0.006,0.006,
      0.006,0.006,0.005,0.006,0.005
    ],
    [
      0.29999999999999716, 0.3999999999999986, 0.3999999999999986, 0.4000000000000057, 0.29999999999999716, 0.7000000000000028, 0.5, 0.5999999999999943, 0.4000000000000057, 0.5,
      0.29999999999999716, 0.10000000000000142, 0.10000000000000142, -0.10000000000000142, -0.10000000000000142, -0.29999999999999716, -0.4000000000000057, -0.29999999999999716,
      -0.29999999999999716, -0.4000000000000057, -0.3999999999999986, -0.5, -0.5, -0.6000000000000014, -0.3999999999999986, -0.6000000000000014, -0.3999999999999986, -0.5, -0.5,
      -0.6000000000000014, -0.5, -0.5999999999999943, -0.20000000000000284, -0.20000000000000284, -0.19999999999999574, -0.20000000000000284, -0.19999999999999574
    ],
    [
      0.0,12.0,11.0,11.0,13.0,10.0,9.0,9.0,9.0,10.0,8.0,8.0,8.0,8.0,11.0,11.0,11.0,9.0,9.0,10.0,11.0,21.0,10.0,8.0,10.0,10.0,9.0,7.0,7.0,10.0,10.0,10.0,7.0,12.0,9.0,9.0,19.0
    ]
  )
]

@pytest.mark.parametrize("points, expected_distances, expected_eles, expected_times", test_cases_segment)
def test_segment_get_deltas(points, expected_distances, expected_eles, expected_times):
  """Test that Segment correctly calculates deltas between points."""
  segment = Segment(points)
  deltas = segment.get_deltas()

  assert len(deltas) == len(expected_distances)
  for delta, expected_distance, expected_ele, expected_time in zip(deltas, expected_distances, expected_eles, expected_times):
    print(f"Actual: distance={delta.d_distance}, elevation={delta.d_ele}, time={delta.d_time.total_seconds()}")
    print(f"Expected: distance={expected_distance}, elevation={expected_ele}, time={expected_time}")
    assert delta.d_distance == pytest.approx(expected_distance, rel=1e-1)
    assert delta.d_ele == pytest.approx(expected_ele, rel=1e-1)
    assert delta.d_time.total_seconds() == pytest.approx(expected_time, rel=1e-1)

def test_segment_initialization():
  """Test that Segment initializes correctly with points."""
  points = [
    Point(38.8895, -77.0091, 34.0, datetime(2024, 7, 4, 12, 0, 0)),
    Point(38.8977, -77.0365, 30.0, datetime(2024, 7, 4, 12, 0, 6)),
  ]
  segment = Segment(points)
  assert segment.points == points
  assert segment.deltas is None

def test_segment_get_deltas_no_force():
  """Test that get_deltas does not recalculate if deltas already exist."""
  points = [
    Point(38.8895, -77.0091, 34.0, datetime(2024, 7, 4, 12, 0, 0)),
    Point(38.8977, -77.0365, 30.0, datetime(2024, 7, 4, 12, 0, 6)),
  ]
  segment = Segment(points)
  segment.get_deltas()  # First call to calculate deltas
  deltas_before = segment.deltas
  segment.get_deltas(force=False)  # Should not recalculate
  assert segment.deltas == deltas_before  # Deltas should remain the same

def test_segment_get_deltas_force():
  """Test that get_deltas recalculates if force is True."""
  points = [
    Point(38.8895, -77.0091, 34.0, datetime(2024, 7, 4, 12, 0, 0)),
    Point(38.8977, -77.0365, 30.0, datetime(2024, 7, 4, 12, 0, 6)),
  ]
  segment = Segment(points)
  segment.get_deltas()  # First call to calculate deltas
  deltas_before = segment.deltas
  points[0] = Point(38.8896, -77.0092, 34.0, datetime(2024, 7, 4, 12, 0, 0))  # Modify a point
  segment.get_deltas(force=True)  # Force recalculation
  assert segment.deltas != deltas_before  # Deltas should change due to point modification
