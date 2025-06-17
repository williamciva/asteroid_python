import pygame
from typing import Tuple
from recursos.spaceship import Spaceship

## engine
game_resolution: Tuple[int, int] = (1000, 700)
clock_tick: int = 60
clock = pygame.time.Clock()
window = pygame.display.set_mode(game_resolution) 
pygame.display.set_caption("Star Wars Python")


# icons
icon  = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)


## crosshair
crosshair = pygame.image.load("assets/crosshair.png").convert_alpha()



## map
map_limit_x: Tuple[int, int]= (50, game_resolution[0] - 50)
map_limit_y: Tuple[int, int] = (50, game_resolution[1] - 50)


# backgrounds
home_background = pygame.transform.smoothscale(pygame.image.load("assets/home_background.jpg"), game_resolution)
endgame_background = pygame.transform.smoothscale(pygame.image.load("assets/endgame_background.png"), game_resolution)
background = pygame.transform.smoothscale(pygame.image.load("assets/space.png").convert(), game_resolution)


## spaceship
spaceship_res: Tuple[int, int] = (150, 150)
spaceship_x: Tuple[int, int] = (game_resolution[0] / 2) - (spaceship_res[0] / 2)
spaceship_y: Tuple[int, int] = map_limit_x[1]
spaceship = Spaceship(path="assets/mileniumfalcon.png", resolution=spaceship_res, position = (spaceship_x, spaceship_y))


## asteroids
asteroid_res: Tuple[int, int] = (100, 100)
asteroids_range_x: Tuple[int, int] = (0, game_resolution[0] - asteroid_res[0])
init_axle_y: int = -asteroid_res[1]
asteroids_imgs = ("assets/asteroid1.png", "assets/asteroid2.png")

## sounds
musics = { 
    "start_wars_theme": "assets/star_wars_theme.mp3",
    "imperial_march": "assets/imperial_march.mp3"
}

def change_music(ref):
    pygame.mixer.music.load(musics[ref])
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.fadeout(3000)
    pygame.mixer.music.play(-1, fade_ms=2000)

r2d2 = pygame.mixer.Sound("assets/r2d2_sound.mp3")
r2d2.set_volume(0.1)

blaster_cannon = pygame.mixer.Sound("assets/mf_blaster_cannon.mp3")
blaster_cannon.set_volume(0.5)

explosion = pygame.mixer.Sound("assets/explosion.mp3")
explosion.set_volume(0.1)


## fonts
font_small = pygame.font.SysFont("arial", 12)
font = pygame.font.SysFont("arial", 22)
font_big = pygame.font.SysFont("arial", 72)


## colors
white = (255, 255, 255)
black = (0, 0, 0)
dark_grey = (25, 25, 25)
yellow = (255, 255, 0)
black_transparent = (0, 0, 0, 180)
black_transparent_2 = (0, 0, 0, 90)


## filters
filter = pygame.Surface(game_resolution, pygame.SRCALPHA)

filter_transparent = filter
filter_transparent.fill(black_transparent)

filter_transparent_2 = filter
filter_transparent.fill(black_transparent_2)