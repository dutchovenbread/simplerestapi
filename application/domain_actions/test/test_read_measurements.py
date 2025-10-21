import sys
import datetime

import pytest

sys.path.append('.')

from domain_actions.read_files import read_measurements, read_cardio_activities, read_gpx, read_weights, get_gpx_list, get_segments_points_and_times

def test_read_measurements():
  measurements_file = '../test_data/unzipped/healthdata-0001/01-runkeeper-data-export-2019-12-14-032339/measurements.csv'
  data_frame = read_measurements(measurements_file)
  assert len(data_frame) == 4401

def test_read_cardio_activities():
  cardio_activities_file = '../test_data/unzipped/healthdata-0001/01-runkeeper-data-export-2019-12-14-032339/cardioActivities.csv'
  data_frame = read_cardio_activities(cardio_activities_file)
  assert len(data_frame) == 702

def test_read_gpx():
  gpx_file = '../test_data/unzipped/healthdata-0001/01-runkeeper-data-export-2019-12-14-032339/2019-06-01-072353.gpx'
  tree = read_gpx(gpx_file)
  root = tree.getroot()
  assert root.tag == '{http://www.topografix.com/GPX/1/1}gpx'
  track = root[0]
  assert track.tag == '{http://www.topografix.com/GPX/1/1}trk'
  track_segments_count = len(track)
  assert track_segments_count == 17
  track_segment = track[2]
  point_count = len(track_segment)
  assert point_count == 51

def test_get_segments_points_and_times():
  gpx_file = '../test_data/unzipped/healthdata-0001/01-runkeeper-data-export-2019-12-14-032339/2019-06-01-072353.gpx'
  tree = read_gpx(gpx_file)
  segments_points_and_times = get_segments_points_and_times(tree,True)
  segments = len(segments_points_and_times)
  assert segments == 15

  total_points = 0
  for segment in segments_points_and_times:
    print(f'{len(segment)=}')
    total_points += len(segment)
  assert total_points == 1672

  first_segment = segments_points_and_times[0]
  first_point = first_segment[0]
  assert first_point.latitude == pytest.approx(38.771635000)
  assert first_point.longitude == pytest.approx(-77.273426)

  first_time = first_point.time
  assert first_time == datetime.datetime.strptime('2019-06-01T11:23:53Z','%Y-%m-%dT%H:%M:%SZ')

  second_point = first_segment[1]
  assert second_point.distance_delta == pytest.approx(0.00714376116056857)
  assert second_point.elevation_delta == pytest.approx(0.29999999999999716)
  assert second_point.time_delta == pytest.approx(30.0)

def test_read_weights():
  measurements_file = '../test_data/unzipped/healthdata-0001/01-runkeeper-data-export-2019-12-14-032339/measurements.csv'
  data_frame = read_weights(measurements_file)
  assert len(data_frame) == 1293

def test_get_gpx_list():
  cardio_activities_file = '../test_data/unzipped/healthdata-0001/01-runkeeper-data-export-2019-12-14-032339/cardioActivities.csv'
  gpx_list = get_gpx_list(cardio_activities_file)

  assert len(gpx_list) == 612
