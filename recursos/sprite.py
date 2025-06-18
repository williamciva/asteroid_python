import pygame

class Sprite:
    def __init__(self, path, resolution, velocity = 0, position = (0, 0), orientation = "up"):
        self.__orientations = {
            "up": 0,
            "left": 90,
            "down": 180,
            "right": 270
        }
        
        self.path = path
        self.resolution = resolution
        self.width = resolution[0]
        self.height = resolution[1]  
        self.velocity = velocity
        self.position = position
        self.__x = position[0]
        self.__y = position[1]
        self.orientation = orientation
        
        self.__import_image()
        self.__calculate_postion()
        self.__calculate_center()
        self.set_orientation(orientation)
        
    
    def __import_image(self):            
        self.original_sprite = pygame.transform.scale(pygame.image.load(self.path), self.resolution)
        self.sprite = self.original_sprite.copy()
        
    def __calculate_rect(self):
        self.rect = self.sprite .get_rect(center=self.center)
    
    def __calculate_postion(self):
        self.position = (self.__x, self.__y)
        
    def __calculate_center(self):
        self.center = (self.__x, self.__y)
        
    def __calculate_mask(self):
        self.mask = pygame.mask.from_surface(self.sprite)
        bounding_rects = self.mask.get_bounding_rects()
        if bounding_rects:
            self.visible_rect = bounding_rects[0]
        else:
            self.visible_rect = self.rect
        
    def get_mask_and_offset(self, other_sprite):
        offset = (int(other_sprite.rect.x - self.rect.x), int(other_sprite.rect.y - self.rect.y))
        return self.mask, offset

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def set_orientation(self, orientation):
        self.sprite = pygame.transform.rotate(self.original_sprite, self.__orientations[orientation])
        self.__calculate_rect()
        self.__calculate_mask()
    
    def set_rotation(self, angle):
        self.sprite = pygame.transform.rotate(self.original_sprite, angle)
        self.__calculate_rect() 
        self.__calculate_mask()
        
    def set_x(self, pos):
        self.__x = pos
        self.__calculate_postion()
        self.__calculate_center()
        self.__calculate_rect()
        self.__calculate_mask()
        
    def set_y(self, pos):
        self.__y = pos
        self.__calculate_postion()
        self.__calculate_center()
        self.__calculate_rect()
        self.__calculate_mask()