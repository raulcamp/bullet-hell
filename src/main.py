"""Bullet Hell (temp name)"""
import sys
import random
import pygame
from entities import Player, Enemy
from constants import (
    WIDTH,
    HEIGHT,
    PLAYER_WIDTH,
    PLAYER_HEIGHT,
    ENEMY_WIDTH,
    ENEMY_HEIGHT,
    BLACK,
    WHITE,
    RED,
)


class Game:
    """Represents a game"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player = Player(
            PLAYER_WIDTH, PLAYER_HEIGHT, RED,
            width // 2 - PLAYER_WIDTH // 2,
            height // 2 - PLAYER_HEIGHT // 2)
        self.enemies = []

    def update(self):
        """Update game state"""
        for enemy in self.enemies:
            enemy.update_pos()
            if collision(enemy, self.player):
                self.enemies.remove(enemy)
        if not random.randrange(5):
            self.add_enemy()

    def add_enemy(self):
        """Generates a new Enemy"""
        if random.getrandbits(1):
            x = random.randint(0 - ENEMY_WIDTH, self.width)
            y = random.choice([0 - ENEMY_HEIGHT, self.height])
        else:
            x = random.choice([0 - ENEMY_WIDTH, self.width])
            y = random.randint(0 - ENEMY_HEIGHT, self.height)
        tx, ty = self.player.get_x(), self.player.get_y()
        time = 200  # TODO: make constant
        dx = (tx - x) / time
        dy = (ty - y) / time
        enemy = Enemy(ENEMY_WIDTH, ENEMY_HEIGHT, WHITE, x, y, dx, dy)
        self.enemies.append(enemy)
        return enemy

    def draw(self, screen):
        """Draw the current game objects"""
        draw_rect(screen, self.player)
        for enemy in self.enemies:
            draw_rect(screen, enemy)


def collision(obj1, obj2):
    """Checks if two objects collide"""
    obj1x, obj1y = obj1.get_x(), obj1.get_y()
    obj2x, obj2y = obj2.get_x(), obj2.get_y()
    if obj1x < obj2x + obj2.width \
            and obj1x + obj1.width > obj2x:
        if obj1y < obj2y + obj2.height \
                and obj1y + obj1.height > obj2y:
            return True
    return False


def draw_rect(screen, obj):
    """Draws a Pygame rectangle"""
    color = obj.get_color()
    x, y = obj.get_x(), obj.get_y()
    width, height = obj.get_width(), obj.get_height()
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
