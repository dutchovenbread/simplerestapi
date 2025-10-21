from datetime import datetime

class Point:
  def __init__(self, lat: float, lon: float, ele: float, time: datetime):
    self.lat = lat
    self.lon = lon
    self.ele = ele
    self.time = time

  def to_dict(self) -> dict:
    return {
      'lat': self.lat,
      'lon': self.lon,
      'ele': self.ele,
      'time': self.time.isoformat()  # Convert datetime to ISO format string
    }

  @classmethod
  def from_dict(cls, data: dict):
    return cls(
      lat=data['lat'],
      lon=data['lon'],
      ele=data['ele'],
      time=datetime.fromisoformat(data['time'])  # Convert ISO string back to datetime
    )

  def __repr__(self):
    return f"Point(lat={self.lat}, lon={self.lon}, ele={self.ele}, time={self.time})"

# # Example usage
# # Creating a Point object
# point = Point(52.5200, 13.4050, 34.5, datetime.now())

# # Serialize the Point object to JSON
# point_dict = point.to_dict()
# point_json = json.dumps(point_dict)
# print("Serialized JSON:", point_json)

# # Deserialize the JSON back to a Point object
# point_dict_from_json = json.loads(point_json)
# new_point = Point.from_dict(point_dict_from_json)
# print("Deserialized Point:", new_point)
