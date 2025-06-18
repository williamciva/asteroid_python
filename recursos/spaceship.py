import pygame
import math
from recursos.sprite import Sprite
import recursos.engine as engine


class Spaceship(Sprite):
    img = "assets/mileniumfalcon.png"
    resolution=(150, 150)
    
    
    def __init__(self):      
        super().__init__(
            path=Spaceship.img, 
            resolution=Spaceship.resolution
        )
        
        self.__set_initial_position()
        
    
    def __set_initial_position(self):
        center_x = (engine.game_resolution[0] / 2)
        bottom_y = engine.map_limit_y[1] - self.visible_rect.height

        adjust_x = self.visible_rect.x
        adjust_y = self.visible_rect.y

        self.set_x(center_x - adjust_x)
        self.set_y(bottom_y - adjust_y)
        
    
    def move_spaceship(self, move):
        self.set_x(self.rect.x + move[0])
        self.set_y(self.rect.y + move[1])

        visible = self.visible_rect
        new_x = self.rect.x
        new_y = self.rect.y

        if new_x + visible.x < engine.map_limit_x[0]:
            new_x = engine.map_limit_x[0] - visible.x

        if new_x + visible.x + visible.width > engine.map_limit_x[1]:
            new_x = engine.map_limit_x[1] - visible.width - visible.x

        if new_y + visible.y < engine.map_limit_y[0]:
            new_y = engine.map_limit_y[0] - visible.y

        if new_y + visible.y + visible.height > engine.map_limit_y[1]:
            new_y = engine.map_limit_y[1] - visible.height - visible.y

        self.set_x(new_x)
        self.set_y(new_y)

    def calculate_angle_by_mouse(self, mouse_pos):
        dx = mouse_pos[0] - self.get_center()[0]
        dy = mouse_pos[1] - self.get_center()[1]
        
        angle_rad = math.atan2(-dy, dx)
        angle_deg = math.degrees(angle_rad)
        spaceship_angle =  angle_deg - 90
        
        self.set_rotation(spaceship_angle)
        
    def verify_colision(self, other):
        spaceship_mask, offset = self.get_mask_and_offset(other)
        mask = pygame.mask.from_surface(other.sprite)
        
        if self.rect.colliderect(other.rect):
            if spaceship_mask.overlap(mask, offset):
                return True
        
        return False