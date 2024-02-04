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
    SPEED_FACTOR,
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
            enemy.update_direction_to(self.player, SPEED_FACTOR)
            enemy.update_pos()
            if collision(enemy, self.player):
                self.enemies.remove(enemy)
                self.player.receive_damage(5)
        if not random.randrange(15):
            self.add_enemy()
        for proj in self.player.get_projectiles():
            proj.update_pos()
            if is_out_of_bounds(proj):
                self.player.remove_projectile(proj)
            else:
                for enemy in self.enemies:
                    if collision(enemy, proj):
                        self.player.remove_projectile(proj)
                        self.enemies.remove(enemy)
                        break

    def add_enemy(self):
        """Generates a new Enemy"""
        if random.getrandbits(1):
            x = random.randint(-ENEMY_WIDTH, self.width)
            y = random.choice([-ENEMY_HEIGHT, self.height])
        else:
            x = random.choice([-ENEMY_WIDTH, self.width])
            y = random.randint(-ENEMY_HEIGHT, self.height)
        enemy = Enemy(ENEMY_WIDTH, ENEMY_HEIGHT, WHITE, x, y)
        enemy.update_direction_to(self.player, SPEED_FACTOR)
        self.enemies.append(enemy)
        return enemy

    def player_attack(self, tx, ty):
        """Attack from the player"""
        self.player.shoot_projectile(tx, ty)

    def draw(self, screen):
        """Draw the current game objects"""
        for enemy in self.enemies:
            draw_rect(screen, enemy)
        for proj in self.player.get_projectiles():
            draw_rect(screen, proj)
        draw_rect(screen, self.player)
        draw_rect(screen, self.player.get_health())


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


def valid_move(obj, x, y):
    """Check if the object can move to the given position"""
    if obj.get_x() + x < 0 or obj.get_x() + x > WIDTH - obj.get_width():
        return False
    if obj.get_y() + y < 0 or obj.get_y() + y > HEIGHT - obj.get_height():
        return False
    return True


def is_out_of_bounds(obj):
    """Checks if the object is out of bounds"""
    if obj.x < -obj.get_width() or obj.x > WIDTH:
        return True
    if obj.y < -obj.get_height() or obj.y > HEIGHT:
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

    sleep = 5
    wait = sleep

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
                wait = sleep

        # Check for key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if valid_move(game.player, -5, 0):
                game.player.x -= 5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if valid_move(game.player, 5, 0):
                game.player.x += 5
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if valid_move(game.player, 0, 5):
                game.player.y += 5
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if valid_move(game.player, 0, -5):
                game.player.y -= 5
        mice = pygame.mouse.get_pressed()
        if mice[0]:
            if wait >= sleep:
                tx, ty = pygame.mouse.get_pos()
                game.player_attack(tx, ty)
                wait = 0
            else:
                wait += 1

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
