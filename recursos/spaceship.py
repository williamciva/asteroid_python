from recursos.sprite import Sprite

class Spaceship(Sprite):
    def __init__(self, path, resolution, velocity = 0, position = (0, 0), orientation = "up"):
        super().__init__(path=path, resolution=resolution, velocity=velocity, position=position, orientation=orientation)