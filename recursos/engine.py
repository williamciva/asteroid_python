import pygame
from typing import Tuple


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
map_limit_x: Tuple[int, int]= (10, game_resolution[0] - 10)
map_limit_y: Tuple[int, int] = (10, game_resolution[1] - 10)


# backgrounds
home_background = pygame.transform.smoothscale(pygame.image.load("assets/home_background.jpg"), game_resolution)
endgame_background = pygame.transform.smoothscale(pygame.image.load("assets/endgame_background.png"), game_resolution)
background = pygame.transform.smoothscale(pygame.image.load("assets/space.jpeg").convert(), game_resolution)


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