"""Bullet Hell (temp name) entities, objects, and classes"""
from dataclasses import dataclass


@dataclass
class Object:
    """Represents an object"""
    width: int
    height: int
    color: tuple
    x: int
    y: int
    dx: int = 0
    dy: int = 0

    def get_width(self):
        """Returns the width of the Object"""
        return self.width

    def get_height(self):
        """Returns the height of the Object"""
        return self.height

    def get_color(self):
        """Returns the color of the Object"""
        return self.color

    def get_x(self):
        """Returns the x-coordinate of the Object"""
        return self.x

    def get_y(self):
        """Returns the y-coordinate of the Object"""
        return self.y

    def set_pos(self, nx, ny):
        """Sets the position of the Object"""
        self.x, self.y = nx, ny

    def get_dx(self):
        """Returns the x-velocity of the Object"""
        return self.dx

    def get_dy(self):
        """Returns the y-velocity of the Object"""
        return self.dy

    def set_vel(self, ndx, ndy):
        """Sets the velocity of the Object"""
        self.dx, self.dy = ndx, ndy

    def update_pos(self):
        """Updates the position of the Object"""
        self.set_pos(self.x + self.dx, self.y + self.dy)


@dataclass
class Player(Object):
    """Represents a Player"""


@dataclass
class Enemy(Object):
    """Represents an Enemy"""


if __name__ == "__main__":
    pass
