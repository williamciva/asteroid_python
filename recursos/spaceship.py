import recursos.engine as engine
from recursos.sprite import Sprite

class Spaceship(Sprite):
    def __init__(self):      
        super().__init__(
            path="assets/mileniumfalcon.png", 
            resolution=(150, 150)
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
        spaceship_x, spaceship_y = self.position
        self.set_x(spaceship_x + move[0])
        self.set_y(spaceship_y + move[1])

        adjust_x = self.visible_rect.x
        adjust_y = self.visible_rect.y

        if spaceship_x < engine.map_limit_x[0]:
            self.set_x(engine.map_limit_x[0])
        elif spaceship_x > engine.map_limit_x[1] - self.resolution[0]:
            self.set_x(engine.map_limit_x[1] - self.resolution[0])
        
        if spaceship_y < engine.map_limit_y[0]:
            self.set_y(engine.map_limit_y[0])
        elif spaceship_y > engine.map_limit_y[1] - self.resolution[1]:
            self.set_y(engine.map_limit_y[1] - self.resolution[1])