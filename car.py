import pygame
STARTING_X = 160
STARTING_Y = 500
class Car(pygame.sprite.Sprite):

    # This class represents a car. It derives from the "Sprite" class in Pygame.

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
        self.invincible = False
        self.invincibility_start_time = 0

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



