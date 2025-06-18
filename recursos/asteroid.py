import pygame
import random
from recursos.sprite import Sprite
import recursos.engine as engine


class Asteroid(Sprite):
    imgs = ("assets/asteroid1.png", "assets/asteroid2.png")
    resolution = (100, 100)
    range_x = (0, engine.game_resolution[0] - resolution[0])
    init_y: int = -resolution[1]
    
    @staticmethod
    def build_random():
        img = Asteroid.imgs[random.randint(0, 1)]
        x = random.randint(Asteroid.range_x[0], Asteroid.range_x[1])
        postion = (x, Asteroid.init_y)
        asteroid = Asteroid(img=img, resolution=Asteroid.resolution, position=postion)
        asteroid.set_rotation(random.randint(0, 359))
        return asteroid
    
    
    def __init__(self, img, resolution, position):
        super().__init__(path=img, resolution=resolution, position=position)
        
        
    def verify_laser_colision(self, laser):
        rel_x = int(laser.x - self.rect.x)
        rel_y = int(laser.y - self.rect.y)

        if 0 <= rel_x < self.rect.width and 0 <= rel_y < self.rect.height:
            mask = pygame.mask.from_surface(self.sprite)
            if mask.get_at((rel_x, rel_y)):
                return True
            
        return False