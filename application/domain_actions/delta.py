import math
from datetime import datetime, timedelta
from domain_actions.point import Point

class Delta:
  def __init__(self, point_a, point_b, climb=None):
    """Initialize a Delta object with two points."""
    self.point_a = point_a
    self.point_b = point_b
    self.d_distance = Delta.calculate_distance(point_a, point_b)
    self.d_ele = point_b.ele - point_a.ele
    self.d_time = point_b.time - point_a.time
    if climb is None:
      self.climb = Delta.calculate_climb(point_a, point_b)
    else:
      self.climb = climb

  @staticmethod
  def calculate_distance(point_a, point_b):
    """Calculate the distance between two points using the Haversine formula."""
    radius_earth = 3958.8  # Radius of the Earth in miles
    lat1 = math.radians(point_a.lat)
    lon1 = math.radians(point_a.lon)
    lat2 = math.radians(point_b.lat)
    lon2 = math.radians(point_b.lon)

    # Differences
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    # Haversine formula
    haversine_formula_component = (math.sin(delta_lat / 2) ** 2 +
      math.cos(lat1) * math.cos(lat2) *
      math.sin(delta_lon / 2) ** 2)
    angular_distance = 2 * math.asin(math.sqrt(haversine_formula_component))

    # Distance in miles
    distance = radius_earth * angular_distance
    return distance

  @staticmethod
  def calculate_climb(point_a, point_b):
    """Calculate the climb between two points."""
    return max(0, point_b.ele - point_a.ele)

  def to_dict(self):
    """Convert the Delta to a dictionary representation."""
    return {
      'd_distance': self.d_distance,
      'd_ele': self.d_ele,
      'd_time': self.d_time.total_seconds(),  # Convert timedelta to seconds for serialization
      'climb': self.climb
    }

  @classmethod
  def from_dict(cls, data):
    """Create a Delta from a dictionary representation."""
    # Since d_time is stored as seconds, we need to convert it back to timedelta
    d_time = timedelta(seconds=data['d_time'])
    delta = cls(Point(0, 0, 0, datetime.now()), Point(0, 0, 0, datetime.now()))  # Placeholder points
    delta.d_distance = data['d_distance']
    delta.d_ele = data['d_ele']
    delta.d_time = d_time
    delta.climb = data['climb']
    return delta

  def __repr__(self):
    """String representation of the Delta."""
    return f"Delta(d_distance={self.d_distance}, d_ele={self.d_ele}, d_time={self.d_time}, climb={self.climb})"
