import os
import xml.etree.ElementTree as ET
from collections import namedtuple
import datetime
import pandas as pd
from geopy import distance

from domain_actions import fix

TrackPoint = namedtuple('TrackPoint',['latitude','longitude','elevation','time','distance_delta','elevation_delta','time_delta'])

def read_generic_csv(local_file):
  # stem = 'file://localhost/'
  # full_path = os.path.join(stem,local_file)
  full_path = local_file
  data_frame = pd.read_csv(full_path)
  return data_frame

def read_measurements(local_file):
  return read_generic_csv(local_file)

def read_weights(local_file):
  data_frame = read_measurements(local_file)
  is_weight = data_frame['Type'] == 'weight'
  return data_frame[is_weight]

def read_cardio_activities(local_file):
  return read_generic_csv(local_file)

def read_fix_gpx(local_file):
  with open(local_file) as text_file:
    text_string = text_file.read()
    print(f'opened file [{local_file}]')
  if fix.needs_fixing(text_string):
    print(f'file needs fixing [{local_file}]')
    string_result = fix.fix(text_string)
    if fix.needs_fixing(string_result):
      print('attempting to fix file [{local_file}] failed. throwing an error')
      read_gpx(local_file)
    else:
      print(f'attempt to fix file [{local_file}] was successful')
    os.rename(local_file, f'{local_file}.corrupt')
    with open(local_file,"w+") as file_write:
      file_write.writelines(string_result)
  return ET.parse(local_file)

def read_gpx(local_file):
  tree = ET.parse(local_file)

  return tree

def get_segments_points_and_times(gpx_contents, deltas = False):
  root = gpx_contents.getroot()
  return_list = []
  # the gpx element is the root

  for track in root:
  # in the root there is one trk tag
    print(f'expecting this to be trk {track.tag=}')
    #the trk tag contains several trkseg tags
    for trkseg in track:
      if trkseg.tag == '{http://www.topografix.com/GPX/1/1}trkseg':
        #the trkseg tags have trkpt tags
        print(f'  expecting this to be trkseg {trkseg.tag}')
        segment_list = []
        prev_track_point = None
        for trkpt in trkseg.findall('{http://www.topografix.com/GPX/1/1}trkpt'):
          #each trkpt has lat and lon attributes
          latitude = float(trkpt.attrib['lat'])
          longitude = float(trkpt.attrib['lon'])
          #it also has an ele tag
          elevation = float(trkpt[0].text)
          #it also has a time tag
          time = datetime.datetime.strptime(trkpt[1].text,'%Y-%m-%dT%H:%M:%SZ')
          if not deltas or prev_track_point is None:
            distance_delta = None
            elevation_delta = None
            time_delta = None
          else:
            distance_delta = float(distance.distance((prev_track_point.latitude,prev_track_point.longitude),
            (latitude,longitude)).miles)
            elevation_delta = elevation - prev_track_point.elevation
            datetime_delta = time - prev_track_point.time
            time_delta = datetime_delta.seconds
          track_point = TrackPoint(latitude, longitude, elevation, time, distance_delta, elevation_delta, time_delta)
          prev_track_point = track_point
          segment_list.append(track_point)
        return_list.append(segment_list)
  return return_list

def get_gpx_list(cardio_activities_file):
  data_frame = read_cardio_activities(cardio_activities_file)
  files_list = data_frame['GPX File'].dropna().tolist()
  return files_list
