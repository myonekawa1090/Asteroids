# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame   
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()  
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    clock = pygame.time.Clock()  
    dt = 0  # delta time, the time since the last frame
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) 
    
    updatables = pygame.sprite.Group() 
    drawables = pygame.sprite.Group()  
    asteroids = pygame.sprite.Group()  
    #asteroidfields = pygame.sprite.Group()  
    shots = pygame.sprite.Group()  
    
    Player.containers = (updatables, drawables)  
    Asteroid.containers = (asteroids, updatables, drawables) 
    AsteroidField.containers = (updatables, )  
    Shot.containers = (shots, updatables, drawables) 
    
    asteroidfield = AsteroidField()  # create an asteroid field object
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        player.draw(screen)  # draw the player
        player.update(dt)  # update the player
        updatables.update(dt) 
        for drawable in drawables:
            drawable.draw(screen)
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game Over!")
                return
        pygame.display.flip()  
        dt = clock.tick(60) / 1000  
    

if __name__ == "__main__":
    main()