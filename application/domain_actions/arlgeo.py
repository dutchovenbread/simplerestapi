from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from domain_actions.grid import STEP_SIZE, get_grid_key, grid_round

arl_corners = [
  (38.934256,-77.119772),
  (38.893264,-77.172235),
  (38.827441,-77.087990),
  (38.843320,-77.085359),
  (38.841206,-77.046294),
  (38.865460,-77.036409),
  (38.901724,-77.069409),
  (38.909456,-77.098390),
]

def is_in_arlington(lat_lon):

  latitude = lat_lon[0]
  longitude = lat_lon[1]
  point = Point(latitude, longitude)
  polygon = Polygon(arl_corners)

  return polygon.contains(point)

def max_lat():
  return max(corner[0] for corner in arl_corners)

def min_lat():
  return min(corner[0] for corner in arl_corners)

def max_lon():
  return max(corner[1] for corner in arl_corners)

def min_lon():
  return min(corner[1] for corner in arl_corners)

def get_arl_gridpoints():
  max_latitude = max_lat() + STEP_SIZE
  min_latitude = min_lat() - STEP_SIZE
  max_longitude = max_lon() + STEP_SIZE
  min_longitude = min_lon() - STEP_SIZE

  lat_number_of_steps = int(round((max_latitude - min_latitude) / STEP_SIZE))
  lon_number_of_steps = int(round((max_longitude - min_longitude) / STEP_SIZE))

  latitudes = [x*STEP_SIZE+grid_round(min_latitude) for x in range(lat_number_of_steps)]
  longitudes = [x*STEP_SIZE+grid_round(min_longitude) for x in range(lon_number_of_steps)]

  points = []
  for latitude in latitudes:
    for longitude in longitudes:
      if is_in_arlington((latitude,longitude)):
        points.append((latitude,longitude))
  return points

def get_arl_gridkeys():
  gridpoints = get_arl_gridpoints()
  keys = []
  for point in gridpoints:
    keys.append(get_grid_key(point))
  return keys
