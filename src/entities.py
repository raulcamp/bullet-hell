"""Bullet Hell (temp name) entities, objects, and classes"""
from dataclasses import dataclass


@dataclass
class Point:
    """Represents a point in 2D space"""
    x: int
    y: int

    def get(self):
        """Returns the coordinates of the point"""
        return self.x, self.y


@dataclass
class Object:
    """Represents an object"""
    coordinates: Point
    width: int
    height: int
    color: tuple


if __name__ == "__main__":
    pass
