import pygame

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


class PlayerCar(Car):
    def __init__(self, image_file, width, height, speed):
        super().__init__(image_file, width, height, speed)
        self.is_traffic_car = False
        self.can_go_through_traffic = False
        self.invincible = False
        self.invincibility_start_time = 0
        self.effect_duration = 8000
        self.score_multiplier = 1

    def reset_powerup(self):
        self.invincible = False
        self.can_go_through_traffic = False
        self.invincibility_start_time = 0


class TrafficCar(Car):
    def __init__(self, image_file, width, height, speed):
        super().__init__(image_file, width, height, speed)
        self.is_traffic_car = True
