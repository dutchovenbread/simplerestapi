import sys

import pytest

sys.path.append('.')
from domain_actions.arlgeo import is_in_arlington, max_lat, min_lat, max_lon, min_lon, get_arl_gridpoints, get_arl_gridkeys

def test_is_in_arlington_0_0():
  result = is_in_arlington((0.0,0.0))
  assert result is not None
  assert not result

@pytest.mark.parametrize(
  "input_lat, input_lon,expected_result",
  [
    (38.929289,-77.119474,True),
    (38.890055,-77.159914,True),
    (38.833011,-77.089172,True),
    (38.848307,-77.044542,True),
    (38.895000,-77.077955,True),
    (38.905818,-77.054358,False),
    (38.932153,-77.139507,False),
    (38.838557,-77.124695,False),
    (38.831952,-77.068750,False),
    (38.851500,-77.011636,False)
  ]
)
def test_is_in_arlington(input_lat, input_lon, expected_result):
  actual_result = is_in_arlington((input_lat,input_lon))
  assert actual_result is not None
  assert actual_result == expected_result

def test_max_lat():
  assert pytest.approx(max_lat(),0.0001) == 38.934256

def test_min_lat():
  assert pytest.approx(min_lat(),0.0001) == 38.827441

def test_max_lon():
  assert pytest.approx(max_lon(),0.0001) == -77.036409

def test_min_lon():
  assert pytest.approx(min_lon(),0.0001) == -77.172235

def test_get_arl_gridpoints():
  gridpoints = get_arl_gridpoints()
  assert len(gridpoints) == 1760

def test_get_arl_gridkeys():
  grid_keys = get_arl_gridkeys()
  assert len(grid_keys) == 1760
  assert grid_keys[0] == '038828282912'
