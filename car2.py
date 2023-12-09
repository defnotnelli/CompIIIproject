"""
Car Module

This module defines the Car class and its subclasses.

Classes:
    - Car: Represents a generic car with basic movement and speed attributes.
    - PlayerCar: Inherits from Car, representing the player's car with additional features.
    - TrafficCar: Inherits from Car, representing traffic cars with a slowing effect.

Usage:
    - Instantiate the Car class to create a generic car.
    - Instantiate the PlayerCar class to create the player's car with special features.
    - Instantiate the TrafficCar class to create traffic cars with slowing effects.

Attributes and Methods:
    - Car:
        - moveRight, moveLeft, moveForward, moveBackward: Move the car in different directions.
        - changeSpeed: Modify the car's speed.
        - load_car_image: Load a new image for the car.
        - update: Placeholder method for potential future updates.

    - PlayerCar (Inherits from Car):
        - reset_powerup: Reset power-up attributes for the player's car.
        - apply_original_image: Reset the player's car to its original image.
        - update: Check and reset invincibility and score divider effects.
        - apply_powerup: Apply power-up effects to the player's car.

    - TrafficCar (Inherits from Car):
        - update: Check and reset slowing effects for traffic cars.
        - affect_powerup: Apply slowing effects to traffic cars.

"""


import pygame

from powerup import SlowingPowerUp,InvincibilityPowerUp

STARTING_X = 160
STARTING_Y = 500


class Car(pygame.sprite.Sprite):

    def __init__(self, image_file, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Instead we could load a proper picture of a car...
        self.image = pygame.image.load(image_file).convert_alpha()

        # Resize the image to match the car´s height and width
        self.image = pygame.transform.scale(self.image, (width, height))

        # Initialise attributes of the car.
        self.width = width
        self.height = height
        self.speed = speed

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20

    def moveBackward(self, speed):
        self.rect.y -= self.speed * speed / 20

    def changeSpeed(self, speed):
        self.speed = speed

    def load_car_image(self, image_file):
        new_image = pygame.image.load(image_file).convert_alpha()
        self.image = pygame.transform.scale(new_image, (self.width, self.height))

    def update(self):
        pass


class PlayerCar(Car):
    def __init__(self, image_file, width, height, speed):
        super().__init__(image_file, width, height, speed)
        self.is_traffic_car = False
        self.can_go_through_traffic = False
        self.invincible = False
        self.invincibility_start_time = 0
        self.effect_duration = 9000
        self.score_divider = 1
        self.score = 0
        self.score_divider_exp_time = 0
        self.original_image = pygame.image.load("RedRari.png").convert_alpha()






    def reset_powerup(self):
        self.invincible = False
        self.invincibility_start_time = 0
        self.score_divider = 1
        self.score_divider_exp_time = 0
        self.apply_original_image()

    def apply_original_image(self):
        # Reset to the original image
        self.image = pygame.transform.scale(self.original_image, (self.width, self.height))



    def update(self):
        if self.invincible:
            # Check if the invincibility duration has expired
            current_time = pygame.time.get_ticks()
            if current_time >= self.invincibility_start_time + self.effect_duration:
                self.reset_powerup()  # Reset power-up attributes after the invincibility duration

        if self.score_divider > 1:
            current_time = pygame.time.get_ticks()
            if current_time >= self.score_divider_exp_time + self.effect_duration:
                self.reset_powerup()

    def apply_powerup(self, powerup):

        if isinstance(powerup, InvincibilityPowerUp):
            powerup.affect_player(self)

    def apply_score_divider(self, divider):
        self.score_divider = divider
        self.score_divider_exp_time = pygame.time.get_ticks()  # Record start time
        self.score = int(self.score * divider)


class TrafficCar(Car):
    def __init__(self, image_file, width, height, speed):
        super().__init__(image_file, width, height, speed)
        self.is_traffic_car = True
        self.effect_duration = 10000
        self.slowed = False
        self.slowed_start_time = 0

    def update(self):

        # Check if the slowing effect has expired
        if self.slowed:
            current_time = pygame.time.get_ticks()
            if current_time >= self.slowed_start_time + self.effect_duration:
                self.reset_powerup()

    def affect_powerup(self, powerup):
        if isinstance(powerup, SlowingPowerUp):
            powerup.affect_traffic(self)
            self.slowed = True

    def reset_powerup(self):
        self.slowed = False
        self.slowed_start_time = 0
