"""Bullet Hell (temp name) entities, objects, and classes"""
from dataclasses import dataclass, field
import math
from constants import (
    WIDTH,
    PROJECTILE_WIDTH,
    PROJECTILE_HEIGHT,
    PROJECTILE_SPEED_FACTOR,
    RED,
    GREEN,
)


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

    def update_direction_to(self, other, factor):
        """Updates the velocity and direction to other Object"""
        tx, ty = other.get_x(), other.get_y()
        xv, yv = (tx - self.get_x()), (ty - self.get_y())
        norm = math.sqrt(xv**2 + yv**2)
        dx = factor * xv / norm
        dy = factor * yv / norm
        self.set_vel(dx, dy)


@dataclass
class Projectile(Object):
    """Represents a Projectile"""


@dataclass
class Health:
    """Represents a healthbar"""
    width: int = 0.9*WIDTH
    o_width: int = 0.9*WIDTH
    height: int = 15
    color: tuple = RED
    x: int = 20
    y: int = 20
    hp: int = 100
    max_hp: int = 100

    def get_width(self):
        """Returns the width of the healthbar"""
        return self.width

    def get_height(self):
        """Returns the height of the healthbar"""
        return self.height

    def get_color(self):
        """Returns the color of the healthbar"""
        return self.color

    def get_x(self):
        """Returns the x-coordinate of the healthbar"""
        return self.x

    def get_y(self):
        """Returns the y-coordinate of the healthbar"""
        return self.y

    def get_hp(self):
        """Returns the hp of the healthbar"""
        return self.hp

    def damage(self, amount):
        """Update the healthbar with amount of damage"""
        self.hp -= amount
        self.hp = max(self.hp, 0)
        self.width = self.o_width * (self.hp / self.max_hp)


@dataclass
class Player(Object):
    """Represents a Player"""
    projectiles: list = field(default_factory=list)

    def __post_init__(self):
        self.health = Health()

    def get_health(self):
        """Gets the player's health"""
        return self.health

    def receive_damage(self, amount):
        """Recieve damage for the player"""
        self.get_health().damage(amount)

    def is_dead(self):
        """Check if the player is dead"""
        return not self.get_health().get_hp()

    def get_projectiles(self):
        """Gets the player's fired projectiles"""
        return self.projectiles

    def shoot_projectile(self, tx, ty):
        """Shoot a Projectile"""
        x, y = self.get_x() + self.width // 2, self.get_y() + self.height // 2
        xv, yv = (tx - x), (ty - y)
        norm = math.sqrt(xv**2 + yv**2)
        dx = PROJECTILE_SPEED_FACTOR * xv / norm
        dy = PROJECTILE_SPEED_FACTOR * yv / norm
        proj = Projectile(
            PROJECTILE_WIDTH, PROJECTILE_HEIGHT, GREEN, x, y, dx, dy)
        self.projectiles.append(proj)
        return proj

    def remove_projectile(self, proj):
        """Removes the projectile"""
        self.projectiles.remove(proj)


@dataclass
class Enemy(Object):
    """Represents an Enemy"""


if __name__ == "__main__":
    pass
