from datetime import datetime

import pytest

from domain_actions.timegridkey import get_time_grid_key, get_date, get_lat_lon, get_type

@pytest.mark.parametrize(
  "lat,lon,datetime_str,activity_type,expected_lat, expected_lon, expected_date_str, expected_type",
  [
    (5.000,10.000,"2021-01-01 14:40:00","Hiking",5.000,10.000,'2021-01-01',"Hiking"),
    (10.001,20.001,"2021-01-02 14:40:00","Walking",10.002,20.002,'2021-01-02',"Walking"),
    (10.0005,30.0005,"2021-03-01 14:40:00","Running",10.001,30.001,'2021-03-01',"Running"),
    (-20.0005,-40.0004,"2022-01-01 14:40:00","Cycling",-20.000,-40.000,'2022-01-01',"Cycling")
  ]
)
def test_round_trip(lat,lon,datetime_str,activity_type,expected_lat,expected_lon,expected_date_str,expected_type):
  datetime_obj = datetime.fromisoformat(datetime_str)
  key = get_time_grid_key(lat,lon,datetime_obj,activity_type)
  lat_lon = get_lat_lon(key)
  type = get_type(key)
  date_string = datetime_obj.strftime('%Y-%m-%d')
  assert lat_lon[0] == pytest.approx(expected_lat,.001)
  assert lat_lon[1] == pytest.approx(expected_lon,.001)
  assert type == expected_type
  assert date_string == expected_date_str

@pytest.mark.parametrize(
  "lat,lon,datetime_str,activity_type,expected_key",
  [
    (15.000,10.000,"2021-01-01 14:40:00","Hiking",'20210101015000010000HIKE'),
    (11.001,20.001,"2021-01-02 14:40:00","Walking",'20210102011000020002WALK'),
    (12.0005,30.0005,"2021-03-01 14:40:00","Running",'20210301012000030000RUNN'),
    (-20.0005,-41.0004,"2022-01-01 14:40:00","Cycling",'20220101340000319000BIKE')
  ]
)
def test_get_time_grid_key(lat,lon,datetime_str,activity_type,expected_key):
  datetime_obj = datetime.fromisoformat(datetime_str)
  actual_result_key = get_time_grid_key(lat,lon,datetime_obj,activity_type)
  assert actual_result_key == expected_key


@pytest.mark.parametrize(
  "key,expected_lat, expected_lon",
  [
    ('20210101006000010000HIKE',6.000,10.000),
    ('20210102016002020002WALK',16.002,20.002),
    ('20210301017000030000RUNN',17.000,30.000),
    ('20220101340000313000BIKE',-20.000,-47.000)
  ]
)
def test_get_lat_lon_grid_key(key,expected_lat, expected_lon):
  actual_result = get_lat_lon(key)
  assert actual_result == (expected_lat, expected_lon)

@pytest.mark.parametrize(
  "key,expected_date_string",
  [
    ('20210101035000010000HIKE',"2021-01-01"),
    ('20210102010001050001WALK',"2021-01-02"),
    ('20210301010000080000RUNN',"2021-03-01"),
    ('20220101340000300000BIKE','2022-01-01')
  ]
)
def test_get_date(key,expected_date_string):
  actual_result = get_date(key)
  date_result_string = actual_result.strftime('%Y-%m-%d')
  assert date_result_string == expected_date_string

@pytest.mark.parametrize(
  "key,expected_type",
  [
    ('20210101035000010000HIKE',"Hiking"),
    ('20210102010001050001WALK',"Walking"),
    ('20210301010000080000RUNN',"Running"),
    ('20220101340000300000BIKE','Cycling')
  ]
)
def test_get_type(key,expected_type):
  actual_result = get_type(key)

  assert actual_result == expected_type
