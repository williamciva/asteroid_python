from recursos.sprite import Sprite

class Asteroid(Sprite):
    def __init__(self, path, resolution, position, velocity = 0, orientation = "up"):
        super().__init__(path=path, resolution=resolution, velocity=velocity, position=position, orientation=orientation)