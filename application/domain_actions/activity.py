import xml.etree.ElementTree as ET

from datetime import datetime, timedelta, timezone
from domain_actions.segment import Segment
from domain_actions.delta import Delta
from domain_actions.point import Point

class Activity:
  def __init__(self, name, date, segments, a_type):
    self.name = name
    self.date = date
    self.segments = segments
    self.a_type = a_type

  def add_segment(self, segment):
    """Add a segment to the activity."""
    self.segments.append(segment)

  def get_deltas(self, force=False):
    """Get all deltas for the activity."""
    all_deltas = []
    for segment in self.segments:
      deltas = segment.get_deltas(force)
      all_deltas.extend(deltas)
    return all_deltas

  def get_splits(self, split_length):
    """Calculate split deltas based on the provided split length."""
    deltas = self.get_deltas()
    splits = []
    accumulated_distance = 0.0
    accumulated_ele = 0.0
    accumulated_time = timedelta()
    accumulated_climb = 0.0

    for delta in deltas:
      accumulated_distance += delta.d_distance
      accumulated_ele += delta.d_ele
      accumulated_time += delta.d_time
      accumulated_climb += delta.climb

      while accumulated_distance >= split_length:
        split_delta = Delta(
          Point(0, 0, 0, datetime.now()),  # Placeholder points
          Point(0, 0, 0, datetime.now())
        )
        split_delta.d_distance = split_length
        split_delta.d_ele = accumulated_ele
        split_delta.d_time = accumulated_time
        split_delta.climb = accumulated_climb

        splits.append(split_delta)

        accumulated_distance -= split_length
        accumulated_ele = 0.0
        accumulated_time = timedelta()
        accumulated_climb = 0.0

    return splits

  def get_total_climb(self):
    """Calculate the total climb for the activity."""
    total_climb = sum(delta.climb for delta in self.get_deltas())
    return total_climb

  def __repr__(self):
    """String representation of the Activity."""
    return f"Activity(name={self.name}, date={self.date}, segments={self.segments}, a_type={self.a_type})"


  def to_dict(self):
    """Convert the Activity to a dictionary."""
    return {
      'name': self.name,
      'date': self.date.isoformat(),
      'segments': [segment.to_dict() for segment in self.segments],
      'a_type': self.a_type
    }

  @classmethod
  def from_dict(cls, data):
    """Create an Activity from a dictionary."""
    name = data['name']
    date = datetime.fromisoformat(data['date'])
    segments = [Segment.from_dict(seg) for seg in data['segments']]
    a_type = data['a_type']
    return cls(name=name, date=date, segments=segments, a_type=a_type)

def get_tree_from_gpx_file(gpx_file_path):
  """Parse a GPX file and return its XML tree."""
  tree = ET.parse(gpx_file_path)
  return tree

def get_tree_from_gpx_string(gpx_string):
  """Parse a GPX string and return its XML tree."""
  root = ET.fromstring(gpx_string)
  tree = ET.ElementTree(root)
  return tree


def gpx_to_activity(gpx_file_path, path_not_string=True):
  """Convert a GPX file to an Activity object."""
  if path_not_string:
    tree = get_tree_from_gpx_file(gpx_file_path)
  else:
    tree = get_tree_from_gpx_string(gpx_file_path)

  root = tree.getroot()

  # Extract metadata
  name = root.find('.//{http://www.topografix.com/GPX/1/1}name').text
  time_str = root.find('.//{http://www.topografix.com/GPX/1/1}time').text
  date = datetime.fromisoformat(time_str.replace('Z', '+00:00')).astimezone(timezone.utc)

  # Extract type from the first word of the name
  if name is not None:
    a_type = name.split()[0]
  else:
    a_type = None
  print (f'{a_type=}')

  # Extract segments
  segments = []
  for trkseg in root.findall('.//{http://www.topografix.com/GPX/1/1}trkseg'):
    points = []
    for trkpt in trkseg.findall('{http://www.topografix.com/GPX/1/1}trkpt'):
      lat = float(trkpt.attrib['lat'])
      lon = float(trkpt.attrib['lon'])
      ele = float(trkpt.find('{http://www.topografix.com/GPX/1/1}ele').text)
      time_str = trkpt.find('{http://www.topografix.com/GPX/1/1}time').text
      time = datetime.fromisoformat(time_str.replace('Z', '+00:00')).astimezone(timezone.utc)
      points.append(Point(lat, lon, ele, time))
    segment = Segment(points)
    segments.append(segment)

  # Create an activity with the segments
  activity = Activity(segments=segments, name=name, date=date, a_type=a_type)

  return activity
