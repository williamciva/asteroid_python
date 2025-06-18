import pygame
import math

class Laser:
    def __init__(self, start_pos, target_pos, color=(255, 0, 0), speed=25, length=25):
        self.x, self.y = start_pos
        self.color = color
        self.speed = speed
        self.length = length
        self.alive = True

        angle = math.atan2(target_pos[1] - self.y, target_pos[0] - self.x)
        self.dx = math.cos(angle) * self.speed
        self.dy = math.sin(angle) * self.speed
        self.angle = angle

    def update(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self, surface):
        end_x = self.x + math.cos(self.angle) * self.length
        end_y = self.y + math.sin(self.angle) * self.length

        pygame.draw.line(surface, self.color, (self.x, self.y), (end_x, end_y), 4)

    def get_position(self):
        return int(self.x), int(self.y)
