import pygame
import random
import car
from abc import ABC, abstractmethod

GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
BLACK = (0,0,0)
shade_of_purple = (255, 0, 255)


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

    def moveForward(self, pixels):
        self.rect.y += pixels
        self.effect_duration -= pixels
        if self.effect_duration <= 0:
            self.kill()

class InvincibilityPowerUp(PowerUp):
    def __init__(self):
        super().__init__("invincibility.png", 30, 30, 8000)  # Increased duration

    def affect_player(self, player):
        player.invincible = True
        player.invincibility_start_time = pygame.time.get_ticks()

    def affect_traffic(self, traffic_car):
        pass  # No effect on traffic cars

class SlowingPowerUp(PowerUp):
    def __init__(self):
        super().__init__("slowing_powerup.png", 30, 30, 6000)  # Adjusted duration

    def affect_player(self, player):
        pass  # No effect on the player

    def affect_traffic(self, traffic_car):
        traffic_car.changeSpeed(max(1, traffic_car.speed // 2))  # Ensure the minimum speed is 1

class SpeedBoostPowerUp(PowerUp):
    def __init__(self):
        super().__init__("speed_boost_powerup.png", 30, 30, 6000)  # Adjusted duration

    def affect_player(self, player):
        player.changeSpeed(player.speed * 1.5)  # Increased speed boost

    def affect_traffic(self, traffic_car):
        pass  # No effect on traffic cars

class SizeChangePowerUp(PowerUp):
    def __init__(self):
        super().__init__("size_change_powerup.png", 30, 30, 8000)  # Increased duration

    def affect_player(self, player):
        player.width *= 2
        player.height *= 2
        player.image = pygame.transform.scale(player.image, (player.width, player.height))

    def affect_traffic(self, traffic_car):
        pass  # No effect on traffic cars

class TimeFreezePowerUp(PowerUp):
    def __init__(self):
        super().__init__("time_freezes_powerup.png", 30, 30, 5000)  # Standard duration

    def affect_player(self, player):
        # Freeze the game for a short duration
        pygame.time.delay(2000)  # Adjust the duration (2 seconds in this case)

    def affect_traffic(self, traffic_car):
        pass  # No effect on traffic cars

class ScoreMultiplierPowerUp(PowerUp):
    def __init__(self):
        super().__init__("score_multiplier_powerup.png", 30, 30, 8000)  # Increased duration

    def affect_player(self, player):
        # Double the score multiplier for a short duration
        player.score_multiplier *= 2
        pygame.time.delay(6000)  # Adjust the duration (6 seconds in this case)
        player.score_multiplier = 1  # Reset the score multiplier

    def affect_traffic(self, traffic_car):
        pass  # No effect on traffic cars

class RandomLaneChangePowerUp(PowerUp):
    def __init__(self):
        super().__init__("random_line_change_powerup.png", 30, 30, 6000)  # Adjusted duration

    def affect_player(self, player):
        # Randomly change the player's lane for a short duration
        player.random_lane_change_active = True
        pygame.time.delay(3000)  # Adjust the duration (3 seconds in this case)
        player.random_lane_change_active = False

    def affect_traffic(self, traffic_car):
        pass  # No effect on traffic cars

