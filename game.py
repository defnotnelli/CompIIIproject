import pygame, random
# Let's import the Car Class
from car import Car
import os
from powerup import PowerUp


def car_racing():
    pygame.init()

    difficulty_level = 1  # Initial difficulty level

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

    speed = 1
    colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)

    imageList = ["YeRari.png", "BlackRari.png", "BlueRari.png", "McLauren.png"]

    SCREENWIDTH = 900
    SCREENHEIGHT = 600

    size = (SCREENWIDTH, SCREENHEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Djogo di Carru")

    # This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()

    playerCar = Car("RedRari.png", 50, 75, 70)
    playerCar.rect.x = (SCREENWIDTH - playerCar.rect.width) / 2
    playerCar.rect.y = SCREENHEIGHT - 100

    car1 = Car("YeRari.png", 50, 75, random.randint(50, 100))
    car1.rect.x = 275
    car1.rect.y = -300

    car2 = Car("BlackRari.png", 50, 75, random.randint(50, 100))
    car2.rect.x = 375
    car2.rect.y = -600

    car3 = Car("BlueRari.png", 50, 75, random.randint(50, 100))
    car3.rect.x = 475
    car3.rect.y = -1200

    car4 = Car("McLauren.png", 50, 75, random.randint(50, 100))
    car4.rect.x = 575
    car4.rect.y = -900

    # Add the car to the list of objects
    all_sprites_list.add(playerCar)
    all_sprites_list.add(car1)
    all_sprites_list.add(car2)
    all_sprites_list.add(car3)
    all_sprites_list.add(car4)

    all_coming_cars = pygame.sprite.Group()
    all_coming_cars.add(car1)
    all_coming_cars.add(car2)
    all_coming_cars.add(car3)
    all_coming_cars.add(car4)

    cooler_font = pygame.font.SysFont("Eight-Bit Madness", 50)

    def show_game_over_screen(screen, score):
        # screen
        screen.fill(BLACK)

        text1 = cooler_font.render("Game Over", True, (255, 0, 0))
        text_rect = text1.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 - 50))
        screen.blit(text1, text_rect)

        text2 = cooler_font.render(f"Score: {score}", True, WHITE)
        text_rect = text2.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 + 30))
        screen.blit(text2, text_rect)

        lil_sass = cooler_font.render("Forti bu eh cabali", True, (255, 0, 0))
        lil_sass_rect = lil_sass.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 + 100))
        screen.blit(lil_sass, lil_sass_rect)

        pygame.display.flip()
        pygame.time.wait(1000)  # Display the game-over screen for  seconds

    # Load the background image
    background_image = pygame.image.load("gameback.png").convert()

    base_speed = 1  # Set your desired base speed

    traffic_car_speed = base_speed
    frame_counter = 0
    frames_to_increase_difficulty = 250

    # Allowing the user to close the window...
    carryOn = True
    clock = pygame.time.Clock()
    score = 0

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    playerCar.moveRight(10)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerCar.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            playerCar.moveRight(5)
        if keys[pygame.K_UP]:
            speed += 0.03
            playerCar.moveBackward(speed)
        if keys[pygame.K_DOWN]:
            speed += 0.03
            playerCar.moveForward(speed)

        # Update the speed based on the difficulty level
        speed = base_speed * difficulty_level
        frame_counter += 1
        if frame_counter >= frames_to_increase_difficulty:
            frame_counter = 0
            difficulty_level += 0.2  # Increase difficulty level

        # Game Logic
        for car in all_coming_cars:
            car.moveForward(traffic_car_speed * difficulty_level)
            if car.rect.y > SCREENHEIGHT:
                car.changeSpeed(random.randint(50, 100))
                print("Car reached the limit. Changing speed.")
                car.rect.y = -200
                if car == car1:
                    car.rect.x = 250  # Reset car1 to the leftmost lane
                elif car == car2:
                    car.rect.x = 350  # Reset car2 to the middle lane
                elif car == car3:
                    car.rect.x = 450  # Reset car3 to the right lane
                elif car == car4:
                    car.rect.x = 550  # Reset car4 to the rightmost lane
                    car.load_car_image(random.choice(imageList))  # Randomize the car image

            # Update the speed based on the difficulty level
            traffic_car_speed = base_speed * difficulty_level

            for car in all_coming_cars:
                if car.rect.y > SCREENHEIGHT:
                    print("Changing car image")
                    car.load_car_image(random.choice(imageList))

            # Check if there is a car collision
            car_collision_list = pygame.sprite.spritecollide(playerCar, all_coming_cars, False)
            for car in car_collision_list:
                print("Car crash with player!")
                show_game_over_screen(screen, score)
                # End Of Game
                carryOn = False

        score += 1

        all_sprites_list.update()

        # Draw the background image
        screen.blit(background_image, (0, 0))

        # Draw the road surface
        pygame.draw.rect(screen, BLACK, [250, 0, 400, SCREENHEIGHT])

        # Draw the center line
        pygame.draw.line(screen, WHITE, [450, 0], [450, SCREENHEIGHT], 5)

        # Draw the side lines
        pygame.draw.line(screen, WHITE, [250, 0], [250, SCREENHEIGHT], 5)
        pygame.draw.line(screen, WHITE, [350, 0], [350, SCREENHEIGHT], 5)
        pygame.draw.line(screen, WHITE, [550, 0], [550, SCREENHEIGHT], 5)
        pygame.draw.line(screen, WHITE, [650, 0], [650, SCREENHEIGHT], 5)

        text = cooler_font.render(f"Score: {score}", True, shade_of_purple)
        screen.blit(text, (10, 10))

        # Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        all_sprites_list.draw(screen)

        # Refresh Screen
        pygame.display.flip()

        # Number of frames per second e.g. 60
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    car_racing()
