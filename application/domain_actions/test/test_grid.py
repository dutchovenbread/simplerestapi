import sys

import pytest

sys.path.append('.')

from domain_actions.grid import get_grid_key, grid_key_to_lat_lon

def test_grid_key_0():
  input_lat_lon = (0.0, 0.0)
  actual_result = get_grid_key(input_lat_lon)
  expected_result = '000000000000'
  assert actual_result == expected_result

@pytest.mark.parametrize(
  "input_lat, input_lon,expected_result",
  [
    (38.929289,-77.119474,'038930282880'),
    (38.890055,-77.159914,'038890282840'),
    (38.833011,-77.089172,'038834282910'),
    (38.848307,-77.044542,'038848282956'),
    (38.895000,-77.077955,'038896282922'),
    (38.905818,-77.054358,'038906282946'),
    (38.932153,-77.139507,'038932282860'),
    (38.838557,-77.124695,'038838282876'),
    (38.831952,-77.068750,'038832282932'),
    (38.851500,-77.011636,'038852282988')
  ]
)
def test_get_grid_key(input_lat, input_lon, expected_result):
  actual_result = get_grid_key((input_lat,input_lon))
  assert actual_result is not None
  assert actual_result == expected_result

def test_grid_key_to_lat_lon_0():
  input_key = '000000000000'
  expected_result = (0.0,0.0)
  actual_result = grid_key_to_lat_lon(input_key)
  assert pytest.approx(actual_result[0],.001) == expected_result[0]
  assert pytest.approx(actual_result[1],.001) == expected_result[1]

@pytest.mark.parametrize(
  "expected_lat, expected_lon,input_key",
  [
    (38.929289,-77.119474,'038930282880'),
    (38.890055,-77.159914,'038890282840'),
    (38.833011,-77.089172,'038834282910'),
    (38.848307,-77.044542,'038848282956'),
    (38.895000,-77.077955,'038896282922'),
    (38.905818,-77.054358,'038906282946'),
    (38.932153,-77.139507,'038932282860'),
    (38.838557,-77.124695,'038838282876'),
    (38.831952,-77.068750,'038832282932'),
    (38.851500,-77.011636,'038852282988')
  ]
)
def test_grid_key_to_lat_lon(expected_lat, expected_lon,input_key):
  actual_result = grid_key_to_lat_lon(input_key)
  assert actual_result is not None
  assert pytest.approx(actual_result[0],.002) == expected_lat
  assert pytest.approx(actual_result[1],.002) == expected_lon
