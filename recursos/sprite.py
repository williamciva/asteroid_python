import pygame

class Sprite:
    def __init__(self, path, resolution, position=(0, 0)):
        self.__orientations = {
            "up": 0,
            "left": 90,
            "down": 180,
            "right": 270
        }

        self.path = path
        self.resolution = resolution

        self.__import_image()
        self.__set_rect(position)

    def __import_image(self):
        self.original_sprite = pygame.transform.scale(
            pygame.image.load(self.path),
            self.resolution
        )
        self.sprite = self.original_sprite.copy()

    def __set_rect(self, position):
        self.rect = self.sprite.get_rect(topleft=position)
        self.__calculate_mask()

    def __calculate_mask(self):
        self.mask = pygame.mask.from_surface(self.sprite)
        bounding_rects = self.mask.get_bounding_rects()
        if bounding_rects:
            self.visible_rect = bounding_rects[0]
        else:
            self.visible_rect = self.rect.copy()

    def set_orientation(self, orientation):
        angle = self.__orientations.get(orientation, 0)
        self.set_rotation(angle)

    def set_rotation(self, angle):
        self.sprite = pygame.transform.rotate(self.original_sprite, angle)
        center = self.rect.center
        self.rect = self.sprite.get_rect(center=center)
        self.__calculate_mask()

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def set_x(self, x):
        self.rect.x = x

    def set_y(self, y):
        self.rect.y = y

    def set_position(self, position):
        self.rect.topleft = position

    def get_position(self):
        return self.rect.topleft

    def get_center(self):
        return self.rect.center

    def set_center(self, center):
        self.rect.center = center

    def get_mask_and_offset(self, other_sprite):
        offset = (
            int(other_sprite.rect.x - self.rect.x),
            int(other_sprite.rect.y - self.rect.y)
        )
        return self.mask, offset