import pygame
import random
from car2 import PlayerCar, TrafficCar, Car
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

        self.effect_duration = effect_duration

    @abstractmethod
    def affect_player(self, player):
        pass

    @abstractmethod
    def affect_traffic(self, traffic_car):
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

    def moveForward(self, pixels):
        self.rect.y += pixels
        self.effect_duration -= pixels
        if self.effect_duration <= 0:
            self.kill()


# Creating specific PowerUps

# INVINCIBILITY
class InvincibilityPowerUp(PowerUp):
    def __init__(self):
        super().__init__("invincibility.png", 40, 60, 8000)
        self.expire_time = 0

    def affect_player(self, player):
        player.invincible = True
        player.can_go_through_traffic = True
        self.expire_time = pygame.time.get_ticks() + self.effect_duration

        # Check if the power-up has expired
        current_time = pygame.time.get_ticks()
        if current_time >= self.expire_time:
            self.reset_powerup()

    def reset_powerup(self):
        # Reset attributes when the power-up expires
        self.rect.x = -100  # Move off-screen
        self.rect.y = -100  # Move off-screen
        self.expire_time = 0


    def affect_traffic(self, traffic_car):
        pass  # No effect on traffic cars

    def spawn_probability(self):
        # Fixed probability 
        return 0.75 # 20% chance

    def spawn_location(self, road_width, road_height):
        # Calculate random X-coordinate within the road width based on probability
        if random.random() < self.spawn_probability():
            self.rect.x = random.randint(250, 600)
        else:
            # If the probability check fails, set the position off-screen
            self.rect.x = -100

        # Calculate random Y-coordinate within the road height
        self.rect.y = random.randint(0, road_height - self.rect.height)


# SLOWING
class SlowingPowerUp(PowerUp):
    def __init__(self):
        super().__init__("slowing_powerup.png", 60, 70, 10000)

    def affect_player(self, player):
        pass  # No effect on the player

    def affect_traffic(self, traffic_car):
        traffic_car.speed *= 0.5

    def spawn_probability(self):
        # Fixed probability
        return 0  # 85% chance

    def spawn_location(self, road_width, road_height):
        # Calculate random X-coordinate within the road width based on probability
        if random.random() < self.spawn_probability():
            self.rect.x = random.randint(250, 600)
        else:
            # If the probability check fails, set the position off-screen
            self.rect.x = -100

        # Calculate random Y-coordinate within the road height
        self.rect.y = random.randint(0, road_height - self.rect.height)


# SPEED  funciona, at what cost tho?
class SpeedBoostPowerUp(PowerUp):
    def __init__(self):
        super().__init__("speed_boost_powerup.png", 80, 90, 6000)
        self.is_traffic_car = False

    def affect_player(self, player):
        if self.is_traffic_car == False:
            player.changeSpeed(player.speed * 1.5)

    def affect_traffic(self, traffic_car):
        pass  # No effect on traffic cars

    def spawn_probability(self):
        # Fixed probability
        return 0.0  # 60% chance

    def spawn_location(self, road_width, road_height):
        # Calculate random X-coordinate within the road width based on probability
        if random.random() < self.spawn_probability():
            self.rect.x = random.randint(250, 600)
        else:
            # If the probability check fails, set the position off-screen
            self.rect.x = -100

        # Calculate random Y-coordinate within the road height
        self.rect.y = random.randint(0, road_height - self.rect.height)


# SIZE CHANGE
class SizeChangePowerUp(PowerUp):
    def __init__(self):
        super().__init__("size_change_powerup.png", 60, 70, 8000)  # Increased duration

    def affect_player(self, player):
        player.width *= 1.5
        player.height *= 1.5
        player.image = pygame.transform.scale(player.image, (player.width, player.height))

    def affect_traffic(self, traffic_car):
        pass  # No effect on traffic cars

    def spawn_probability(self):
        # Fixed probability
        return 0  # 60% chance

    def spawn_location(self, road_width, road_height):
        # Calculate random X-coordinate within the road width based on probability
        if random.random() < self.spawn_probability():
            self.rect.x = random.randint(250, 600)
        else:
            # If the probability check fails, set the position off-screen
            self.rect.x = -100

        # Calculate random Y-coordinate within the road height
        self.rect.y = random.randint(0, road_height - self.rect.height)


# MULTIPLIER
class ScoreMultiplierPowerUp(PowerUp):
    def __init__(self):
        super().__init__("score_multiplier_powerup.png", 50, 50, 8000)

    def affect_player(self, player):
        # Double the score multiplier
        player.score_multiplier *= 2
        player.score_multiplier = 1  # Reset the score multiplier

    def affect_traffic(self, traffic_car):
        pass  # No effect on traffic cars

    def spawn_probability(self):
        # Fixed probability
        return 0  # 40% chance

    def spawn_location(self, road_width, road_height):
        # Calculate random X-coordinate within the road width based on probability
        if random.random() < self.spawn_probability():
            self.rect.x = random.randint(250, 600)
        else:
            # If the probability check fails, set the position off-screen
            self.rect.x = -100

        # Calculate random Y-coordinate within the road height
        self.rect.y = random.randint(0, road_height - self.rect.height)


SCREENHEIGHT = 600


# Needs review
class RandomLaneChangePowerUp(PowerUp):
    def __init__(self):
        super().__init__("random_line_change_powerup.png", 40, 70, 6000)
        self.lane_positions = [250, 350, 550, 650]

    def affect_player(self, player):
        random_lane = random.choice(self.lane_positions)
        PlayerCar.rect.x = random_lane
        PlayerCar.rect.y = SCREENHEIGHT - 100

    def affect_traffic(self, traffic_car):
        pass  # No effect on traffic cars

    def spawn_probability(self):
        # Fixed probability
        return 0 # 40% chance

    def spawn_location(self, road_width, road_height):
        # Calculate random X-coordinate within the road width based on probability
        if random.random() < self.spawn_probability():
            self.rect.x = random.randint(250, 600)
        else:
            # If the probability check fails, set the position off-screen
            self.rect.x = -100

        # Calculate random Y-coordinate within the road height
        self.rect.y = random.randint(0, road_height - self.rect.height)
