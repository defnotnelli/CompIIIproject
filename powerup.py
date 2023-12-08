"""
Car Racing Game File - PowerUps

Power-ups provide temporary effects to the player and traffic cars.

Usage:
    - Power-ups randomly spawn on the road, providing different effects.

File Structure:
    - The base class 'PowerUp' defines common attributes and abstract methods for power-ups.
    - Specific power-ups (Invincibility, Slowing, Size Change, Score Divider) inherit from 'PowerUp'.
    - Each power-up has unique effects on the player and traffic cars.

Power-Up Effects:
    - Invincibility: Grants invincibility to the player for a duration.
    - Slowing: Slows down traffic cars for a duration.
    - Size Change: Increases the size of the player's car.
    - Score Divider: Reduces the player's score multiplier.

Sound Effects:
    - Each power-up has an associated sound effect that plays when activated.

"""


import pygame
import random
from abc import ABC, abstractmethod

GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
BLACK = (0, 0, 0)
shade_of_purple = (255, 0, 255)

road_width = 400
road_height = 600


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, image_file, width, height, effect_duration):
        super().__init__()

        self.image = pygame.image.load(image_file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.expire_time = 0
        self.width = width
        self.height = height
        self.original_size = (width, height)

        self.effect_duration = effect_duration

    @abstractmethod
    def affect_player(self, player):
        self.expire_time = pygame.time.get_ticks() + self.effect_duration
        pass

    @abstractmethod
    def affect_traffic(self, traffic_car):
        self.expire_time = pygame.time.get_ticks() + self.effect_duration
        pass

    @abstractmethod
    def spawn_probability(self):
        pass

    @abstractmethod
    def spawn_location(self, road_width, road_height):
        pass

    def set_initial_position(self, road_width, road_height):
        # Call the new spawn_location method to set the initial position
        self.spawn_location(road_width, road_height)

    def reset_powerup(self):
        # Reset attributes when the power-up expires
        self.rect.x = -100  # Move off-screen
        self.rect.y = -100  # Move off-screen
        self.expire_time = 0

    def moveForward(self, pixels):
        self.rect.y += pixels

    def check_expiration(self):
        # Check if the power-up has expired and kill it if needed
        current_time = pygame.time.get_ticks()
        if current_time >= self.expire_time:
            self.kill()


# Creating specific PowerUps

# INVINCIBILITY
class InvincibilityPowerUp(PowerUp):
    def __init__(self):
        super().__init__("invincibility.png", 40, 60, 9000)
        self.powerup_sound = pygame.mixer.Sound("invincible_sound.mp3")

    def affect_player(self, player):
        from car2 import PlayerCar
        print("InvincibilityPowerUp applied to player")
        player.invincible = True
        player.invincibility_start_time = pygame.time.get_ticks()
        self.powerup_sound.play()

    def affect_traffic(self, traffic_car):
        print("InvincibilityPowerUp applied to traffic car - No effect")
        pass  # No effect on traffic cars

    def spawn_probability(self):
        # Fixed probability
        return 0.3 # 30% chance

    def spawn_location(self, road_width, road_height):
        # Calculate random X-coordinate within the road width based on probability
        if random.random() < self.spawn_probability():
            self.rect.x = random.randint(250, 500)
        else:
            # If the probability check fails, set the position off-screen
            self.rect.x = -100

        # Calculate random Y-coordinate within the road height
        self.rect.y = random.randint(0, road_height - self.rect.height)


# SLOWING
class SlowingPowerUp(PowerUp):
    def __init__(self):
        super().__init__("slowing_powerup.png", 60, 70, 9000)
        self.expire_time = 0
        self.powerup_sound = pygame.mixer.Sound("go_go.mp3")

    def affect_player(self, player):
        pass  # No effect on the player

    def affect_traffic(self, traffic_car):
        from car2 import TrafficCar
        slowed_speed = traffic_car.speed * 0.05
        traffic_car.changeSpeed(slowed_speed)
        traffic_car.slowed = True
        traffic_car.slowed_start_time = pygame.time.get_ticks()
        self.powerup_sound.play()

    def spawn_probability(self):
        # Fixed probability
        return 0.4  # 40% chance

    def spawn_location(self, road_width, road_height):
        # Calculate random X-coordinate within the road width based on probability
        if random.random() < self.spawn_probability():
            self.rect.x = random.randint(250, 275)
        else:
            # If the probability check fails, set the position off-screen
            self.rect.x = -100

        # Calculate random Y-coordinate within the road height
        self.rect.y = random.randint(0, road_height - self.rect.height)


# SIZE CHANGE
class SizeChangePowerUp(PowerUp):
    def __init__(self):
        super().__init__("size_change_powerup.png", 60, 70, 10000)
        self.expire_time = 0
        self.powerup_sound = pygame.mixer.Sound("damn.mp3")

    def affect_player(self, player):
        print("SizeChangePowerUp applied to player")
        player.width *= 1.5
        player.height *= 1.5
        player.image = pygame.transform.scale(player.original_image, (player.width, player.height))
        self.powerup_sound.play()

        # Set the expiration time
        self.expire_time = pygame.time.get_ticks() + self.effect_duration

    def reset_powerup(self):
        print("SizeChangePowerUp expired - Resetting attributes")
        # Reset attributes when the power-up expires
        self.rect.x = -100  # Move off-screen
        self.rect.y = -100  # Move off-screen
        self.expire_time = 0

    def affect_traffic(self, traffic_car):
        print("SizeChangePowerUp applied to traffic car - No effect")
        pass  # No effect on traffic cars

    def spawn_probability(self):
        # Fixed probability
        return 0.25 # 25% chance

    def spawn_location(self, road_width, road_height):
        # Calculate random X-coordinate within the road width based on probability
        if random.random() < self.spawn_probability():
            self.rect.x = random.randint(250, 500)
        else:
            # If the probability check fails, set the position off-screen
            self.rect.x = -100

        # Calculate random Y-coordinate within the road height
        self.rect.y = random.randint(0, road_height - self.rect.height)


# MULTIPLIER
class ScoreDividerPowerUp(PowerUp):
    def __init__(self):
        super().__init__("score_multiplier_powerup.png", 50, 70, 8000)
        self.expire_time = 0
        self.powerup_sound = pygame.mixer.Sound("possessed_laugh.mp3")

    def affect_player(self, player):
        player.apply_score_divider(0.5)
        self.powerup_sound.play()

    def affect_traffic(self, traffic_car):
        pass  # No effect on traffic cars

    def spawn_probability(self):
        # Fixed probability
        return 0.45 # 45% chance

    def spawn_location(self, road_width, road_height):
        # Calculate random X-coordinate within the road width based on probability
        if random.random() < self.spawn_probability():
            self.rect.x = random.randint(250, 400)
        else:
            # If the probability check fails, set the position off-screen
            self.rect.x = -100

        # Calculate random Y-coordinate within the road height
        self.rect.y = random.randint(0, road_height - self.rect.height)

