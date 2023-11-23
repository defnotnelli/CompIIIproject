import pygame

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
    def __init__(self, image_file):
        super().__init__()
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()

    def affect_player(self, player):
        pass  # Define the power-up effect for each specific power-up

    def update(self, player):
        pass  # Update the power-up state as needed

    def draw(self, screen, player):
        pass  # Draw the power-up on the screen if needed

