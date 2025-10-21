from datetime import datetime
from domain_actions.grid import get_grid_key, grid_key_to_lat_lon

type_table = [
  ("RUNN","Running"),
  ("WALK","Walking"),
  ("BIKE","Cycling"),
  ("HIKE","Hiking")
]

fixed_to_full = {type[0]:type[1] for type in type_table}
full_to_fixed = {type[1]:type[0] for type in type_table}

def get_time_grid_key(lat,lon,datetime_obj,activity_type):
  fixed_type_string = full_to_fixed[activity_type]
  date_string = datetime_obj.strftime('%Y%m%d')
  grid_key = get_grid_key((lat,lon))
  key = f'{date_string}{grid_key}{fixed_type_string}'
  return key
def get_date(key):
  year_string = key[0:4]
  year_int = int(year_string)
  month_string = key[4:6]
  month_int = int(month_string)
  day_string = key[6:8]
  day_int = int(day_string)
  result_date = datetime(year_int,month_int,day_int)
  return result_date
def get_lat_lon(key):
  grid_key = key[8:20]
  lat_lon = grid_key_to_lat_lon(grid_key)
  return lat_lon
def get_type(key):
  type_fixed = key[20:24]
  type_full = fixed_to_full[type_fixed]
  return type_full
