"""Bullet Hell (temp name)"""
import sys
import pygame
import random
from entities import Object
from constants import (
    WIDTH,
    HEIGHT,
    BLACK,
)


class Game:
    """Represents a game"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def update(self):
        """Update game state"""
        pass

    def draw(self, screen):
        """Draw the current game objects"""
        pass


def collision(obj1, obj2):
    """Checks if two objects collide"""
    obj1x, obj1y = obj1.get_pos()
    obj2x, obj2y = obj2.get_pos()
    if obj1x < obj2x + obj2.width \
            and obj1x + obj1.width > obj2x:
        if obj1y < obj2y + obj2.height \
                and obj1y + obj1.height > obj2y:
            return True
    return False


def draw_rect(screen, color, x, y, width, height):
    """Draws a Pygame rectangle"""
    pygame.draw.rect(screen, color, (x, y, width, height))


def draw_background(screen):
    """Draws a background"""
    screen.fill(BLACK)


def main():
    """Initializes and runs the game"""
    # Initialize pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Game')
    # Create a clock object
    clock = pygame.time.Clock()
    # Create a Game object
    game = Game(WIDTH, HEIGHT)

    while True:
        # Fill the background
        draw_background(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pass
                if event.key == pygame.K_SPACE:
                    pass
                if event.key == pygame.K_1:
                    pass
            if event.type == pygame.MOUSEMOTION:
                pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        # Check for key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            pass
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            pass
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            pass
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            pass

        # Draw the grid and current state
        game.draw(screen)
        # Update the game state
        game.update()
        # Update the display
        pygame.display.update()
        # Set the framerate
        clock.tick(60)


if __name__ == "__main__":
    main()
