# Making a generic worldwide grid
STEP_SIZE = 0.002
NUMBER_OF_DIGITS = 3
PRECISION_FACTOR = 2.0 # should be 1, 2, or 5
FORMAT_STRING = f'%07.{NUMBER_OF_DIGITS}'
def grid_round(value):
  key = round(value / PRECISION_FACTOR,NUMBER_OF_DIGITS) * PRECISION_FACTOR
  return key

def get_grid_key(lat_lon):
  # divide by two, round to three decimals, multiply by two
  lat = lat_lon[0]
  if lat >= 0.0:
    effective_lat = lat
  else:
    effective_lat = lat + 360.0
  result_lat = grid_round(effective_lat)
  result_lat_string = f'{result_lat:07.3f}'

  lon = lat_lon[1]
  if lon >= 0.0:
    effective_lon = lon
  else:
    effective_lon = lon + 360.0
  result_lon = grid_round(effective_lon)
  result_lon_string = f'{result_lon:07.3f}'
  result_key = "".join([result_lat_string.replace('.',''),result_lon_string.replace('.','')])
  return result_key

def grid_key_to_lat_lon(grid_key):
  effective_lat = float('.'.join([grid_key[0:3],grid_key[3:6]]))
  if effective_lat > 90.0:
    lat = effective_lat - 360.0
  else:
    lat = effective_lat

  effective_lon = float('.'.join([grid_key[6:9],grid_key[9:12]]))
  if effective_lon > 180.0:
    lon = effective_lon - 360.0
  else:
    lon = effective_lon

  return (lat,lon)
