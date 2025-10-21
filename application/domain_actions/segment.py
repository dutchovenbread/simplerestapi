# domain_actions/segment.py

from domain_actions.point import Point
from domain_actions.delta import Delta  # Assuming Delta class is imported

class Segment:
  def __init__(self, points=None):
    """Initialize a Segment with a list of Point objects and deltas."""
    self.points = points if points is not None else []
    self.deltas = None  # Initialize deltas to None

  def to_dict(self):
    """Convert the Segment to a dictionary representation."""
    return {
      'points': [point.to_dict() for point in self.points],  # Assuming Point has a to_dict method
      'deltas': [delta.to_dict() for delta in self.deltas] if self.deltas else None  # Include deltas in the dictionary representation
    }

  @classmethod
  def from_dict(cls, data):
    """Create a Segment from a dictionary representation."""
    points = [Point.from_dict(point_data) for point_data in data['points']]
    segment = cls(points)
    segment.deltas = data.get('deltas', None)  # Set deltas if present in data
    return segment

  def get_deltas(self, force=False):
    """Calculate the deltas between consecutive points and return them."""
    if self.deltas is None or force:
      self.deltas = []
      for i in range(len(self.points) - 1):
        delta = Delta(self.points[i], self.points[i + 1])
        self.deltas.append(delta)
    return self.deltas  # Return the calculated deltas

  def __repr__(self):
    """String representation of the Segment."""
    return f"Segment(points={self.points}, deltas={self.deltas})"
