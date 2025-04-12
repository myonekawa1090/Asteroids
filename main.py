# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame   
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()  # initialize the pygame library
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # create a window
    clock = pygame.time.Clock()  # create a clock object to control the frame rate
    dt = 0  # delta time, the time since the last frame
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)  # create a player object
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        player.draw(screen)  # draw the player
        player.update(dt)  # update the player
        pygame.display.flip()  # update the display
        dt = clock.tick(60) / 1000  # limit the frame rate to 60 FPS


if __name__ == "__main__":
    main()