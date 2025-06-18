import math
import random
from typing import List

import pygame
pygame.init()

import recursos.input_voice as iv
from recursos.spaceship import Spaceship
from recursos.asteroid import Asteroid
from recursos.laser import Laser
from recursos.functions import writeData, getData
import recursos.engine as engine


def start():
    menu(engine.home_background)


def menu(background):
    engine.change_music("start_wars_theme")
    
    width_start_button = 150
    height_start_button  = 40
    width_quit_button = 150
    height_quit_button  = 40
    
    
    center_position_x_start = (engine.game_resolution[0] - width_start_button) / 2
    center_position_y_start = ((engine.game_resolution[1] - height_start_button) / 2) - 10


    center_position_x_quit = (engine.game_resolution[0] - width_quit_button) / 2
    center_position_y_quit = ((engine.game_resolution[1] + height_quit_button) / 2) + 10


    startTexto = engine.font.render("Iniciar Game", True, engine.white)
    start_text_width , start_text_height = startTexto.get_size()
    center_position_x_start_text = center_position_x_start + (width_start_button - start_text_width) / 2
    center_position_y_start_text = center_position_y_start + (height_start_button - start_text_height) / 2
    
    
    quitTexto = engine.font.render("Sair do Game", True, engine.white)
    quit_text_width , quit_text_height = quitTexto.get_size()
    center_position_x_quit_text = center_position_x_quit + (width_quit_button - quit_text_width) / 2
    center_position_y_quit_text = center_position_y_quit + (height_quit_button - quit_text_height) / 2

    events = []
    startButton = None
    quitButton = None
    pygame.mouse.set_visible(True)
    while True:
        try:
            events = pygame.event.get()
        except Exception as e:
            print(e)
            
        for evento in events:
            if evento.type == pygame.QUIT:
                quit()
                
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(evento.pos):
                    width_start_button = 140
                    height_start_button  = 35
                    
                if quitButton.collidepoint(evento.pos):
                    width_quit_button = 140
                    height_quit_button  = 35

                
            elif evento.type == pygame.MOUSEBUTTONUP:
                if startButton.collidepoint(evento.pos):
                    width_start_button = 150
                    height_start_button  = 40
                    welcome(colect_name())
                    
                if quitButton.collidepoint(evento.pos):
                    width_quit_button = 150
                    height_quit_button  = 40
                    quit()

        engine.window.fill(engine.white)
        engine.window.blit(background, (0,0))
        for i in range(1, 3):
            engine.window.blit(engine.filter_transparent, (0, 0))

        startButton = pygame.draw.rect(engine.window, engine.dark_grey, (center_position_x_start, center_position_y_start, width_start_button, height_start_button), border_radius=15)
        engine.window.blit(startTexto, (center_position_x_start_text, center_position_y_start_text))
        
        quitButton = pygame.draw.rect(engine.window, engine.dark_grey, (center_position_x_quit, center_position_y_quit, width_quit_button, height_quit_button), border_radius=15)
        engine.window.blit(quitTexto, (center_position_x_quit_text, center_position_y_quit_text))
        
        pygame.display.flip()
        engine.clock.tick(60)


def colect_name():
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()

    
    text_spacing = 50
    
    box_center_x = engine.game_resolution[0] / 2
    
    f_1 = "Fale seu nickname em voz alta!"
    f_3 = f"Se seu nickname estiver correto diga sim."
    
    get_nick_txt = engine.font.render(f_1, True, engine.yellow)
    get_nick_txt_width , get_nick_txt_height = get_nick_txt.get_size()
    get_nick_txt_center_x= box_center_x - (get_nick_txt_width / 2)
    get_nick_txt_y = (text_spacing * 4)
    
    confirm_txt = engine.font.render(f_3, True, engine.yellow)
    confirm_txt_width , confirm_txt_height = confirm_txt.get_size()
    confirm_txt_center_x= box_center_x - (confirm_txt_width / 2)


    nick_name = None
    nick_correct = None
    setp = 0
    
    pygame.mouse.set_visible(True)
    while True:
        f_2 = f"Você disse: {nick_name}."
        f_4 = f"Você disse: {nick_correct}"
        
        engine.window.fill(engine.white)
        engine.window.blit(engine.home_background, (0,0))        
        for i in range(1, 5):
            engine.window.blit(engine.filter_transparent, (0, 0))
            
        engine.window.blit(get_nick_txt, (get_nick_txt_center_x, get_nick_txt_y))
        
        if (nick_name != None):
            setp = 1
            nick_txt = engine.font.render(f_2, True, engine.yellow)
            nick_txt_width , nick_txt_height = nick_txt.get_size()
            nick_txt_center_x= box_center_x - (nick_txt_width / 2)
            nick_txt_y = get_nick_txt_y + text_spacing
            engine.window.blit(nick_txt, (nick_txt_center_x, nick_txt_y))
            confirm_txt_y = nick_txt_y + text_spacing
            engine.window.blit(confirm_txt, (confirm_txt_center_x, confirm_txt_y))
            
            if nick_correct != None:
                setp = 2

                if nick_correct != "sim":
                    nick_correct_txt = engine.font.render(f_4, True, engine.yellow)
                    nick_correct_txt_width , nick_correct_txt_height = nick_txt.get_size()
                    nick_correct_txt_center_x= box_center_x - (nick_correct_txt_width / 2)
                    nick_correct_txt_y = confirm_txt_y + text_spacing
                    engine.window.blit(nick_correct_txt, (nick_correct_txt_center_x, nick_correct_txt_y))
                    
                    setp = 3
        
        
        pygame.display.flip()            
        
        if setp == 0:
            iv.speak(f_1)
            nick_name = iv.recognize()
        elif setp == 1:
            iv.speak(f_2, f_3)
            nick_correct = iv.recognize()
        elif setp == 2:
            return nick_name
        elif setp == 3:
            iv.speak(f_4)
            setp = 0
            nick_name = None
            nick_correct = None
            
        engine.clock.tick(engine.clock_tick)
    

def welcome(nick_name):   
    text_spacing = 50
    
    box_center_x = engine.game_resolution[0] / 2
    
    welcome = f"Seja bem vindo {nick_name}!"
    objective = "Seu objetivo é destruir asteroides e evitar colisões, toda vez que destruí-los será adicinado um ponto ao seu placar."
    gameplay = "Você utilizará as setas (↑ ← ↓ →) ou W A S D do seu teclado para se movimentar."
    gameplay_2 = "Utilize o seu mouse para clicar sobre os asteroides e destruí-los."
    
    welcomeTxt = engine.font.render(welcome, True, engine.yellow)
    welcomeTxt_width , welcomeTxt_height = welcomeTxt.get_size()
    welcomeTxt_center_x= box_center_x - (welcomeTxt_width / 2)
    welcomeTxt_center_y = (text_spacing * 4)
    
    loreTxt = engine.font.render(objective, True, engine.yellow)
    loreTxt_width , loreTxt_height = loreTxt.get_size()
    loreTxt_center_x= box_center_x - (loreTxt_width / 2)
    loreTxt_center_y = welcomeTxt_center_y + text_spacing
    
    gameplayTxt = engine.font.render(gameplay, True, engine.yellow)
    gameplay_width , gameplay_height = gameplayTxt.get_size()
    gameplay_center_x= box_center_x - (gameplay_width / 2)
    gameplay_center_y = loreTxt_center_y + text_spacing
    
    gameplayTxt_2 = engine.font.render(gameplay_2, True, engine.yellow)
    gameplay_2_width , gameplay_2_height = gameplayTxt_2.get_size()
    gameplay_2_center_x= box_center_x - (gameplay_2_width / 2)
    gameplay_2_center_y = gameplay_center_y + text_spacing
    
    
    startTxt = engine.font.render("Iniciar", True, engine.white)
    startTxt_width , startTxt_height = startTxt.get_size()
    startTxt_center_x= box_center_x - (startTxt_width / 2)
    startTxt_center_y = gameplay_center_y + (text_spacing * 3)
    
    start_box_width = startTxt_width + 100
    start_box_height = startTxt_height + 20
    start_box_center_x = box_center_x - (start_box_width / 2)
    start_box_center_y = startTxt_center_y - 10
    
    first_loop = True
    start_button = None
    
    pygame.mouse.set_visible(True)
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
                
            if start_button != None:
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(evento.pos):
                        start_box_width -= 10
                        start_box_height -= 5

                    
                elif evento.type == pygame.MOUSEBUTTONUP:
                    if start_button.collidepoint(evento.pos):
                        start_box_width += 10
                        start_box_height += 5
                        iv.restart_engine()
                        play(nick_name)
        
        engine.window.fill(engine.white)
        engine.window.blit(engine.home_background, (0,0))        
        for i in range(1, 3):
            engine.window.blit(engine.filter_transparent, (0, 0))
            
        engine.window.blit(welcomeTxt, (welcomeTxt_center_x, welcomeTxt_center_y))
        engine.window.blit(loreTxt, (loreTxt_center_x, loreTxt_center_y))
        engine.window.blit(gameplayTxt, (gameplay_center_x, gameplay_center_y))
        engine.window.blit(gameplayTxt_2, (gameplay_2_center_x, gameplay_2_center_y))
        start_button = pygame.draw.rect(engine.window, engine.dark_grey, (start_box_center_x, start_box_center_y, start_box_width, start_box_height), border_radius=15)
        engine.window.blit(startTxt, (startTxt_center_x, startTxt_center_y))
        
        pygame.display.flip()
        
        if(first_loop):
            iv.speak(welcome, objective, gameplay, gameplay_2, is_async=True)
            first_loop = False
        
        engine.clock.tick(engine.clock_tick)


def play(nick_name):
    count = 0
    max_count = 120
    difficulty = 1
    
    move_x  = 0
    move_y  = 0
    
    points = 0
    
    is_paused = False
    pause = False
    
    spaceship = Spaceship()
    asteroids: List[Asteroid] = [Asteroid.build_random()]        
    lasers: List[Laser] = []   
        
    def shoot_laser(mouse_click):
        laser = Laser(start_pos=(spaceship.rect.centerx, spaceship.rect.centery), target_pos=mouse_click)
        lasers.append(laser)
        pygame.mixer.Sound.play(engine.blaster_cannon)
 
    
    pygame.mouse.set_visible(False)
    while True:
        mouse_click = None
        
        for evento in pygame.event.get():
            
            if evento.type == pygame.QUIT:
                quit()
                
            elif evento.type == pygame.KEYUP and (evento.key == pygame.K_RIGHT or evento.key == pygame.K_d):
                move_x = 0
            elif evento.type == pygame.KEYUP and (evento.key == pygame.K_LEFT or evento.key == pygame.K_a):
                move_x = 0
            elif evento.type == pygame.KEYUP and (evento.key == pygame.K_UP or evento.key == pygame.K_w):
                move_y = 0
            elif evento.type == pygame.KEYUP and (evento.key == pygame.K_DOWN or evento.key == pygame.K_s):
                move_y = 0
                
            elif evento.type == pygame.KEYDOWN and (evento.key == pygame.K_RIGHT or evento.key == pygame.K_d):
                move_x = 15
            elif evento.type == pygame.KEYDOWN and (evento.key == pygame.K_LEFT or evento.key == pygame.K_a):
                move_x = -15
            elif evento.type == pygame.KEYDOWN and (evento.key == pygame.K_UP or evento.key == pygame.K_w):
                move_y = -15
            elif evento.type == pygame.KEYDOWN and (evento.key == pygame.K_DOWN or evento.key == pygame.K_s):
                move_y = 15
                
            elif evento.type == pygame.MOUSEBUTTONUP:
                if evento.button == 1:
                    mouse_click = pygame.mouse.get_pos()
                    shoot_laser(mouse_click)
                    
            elif evento.type == pygame.KEYDOWN and evento.key == (pygame.K_SPACE):
                if is_paused:
                    is_paused = False
                    pause = False
                else:
                    is_paused = True
                    pause = True
                
                                
               
        if is_paused:
            if pause:  
                engine.window.blit(engine.filter_transparent, (0, 0))

                texto_pause = engine.font_big.render("PAUSE", True, engine.yellow)
                texto_rect = texto_pause.get_rect(center=(engine.game_resolution[0] // 2, engine.game_resolution[1] // 2))
                engine.window.blit(texto_pause, texto_rect)
                
                pause = False
        
        
        else:                    
            ## increment levels
            count += (1 * difficulty)
            difficulty += 0.005
            if (count >= max_count):
                count = 0
                asteroids.append(Asteroid.build_random())
                
                
            ## configure crosshair
            mouse_x, mouse_y = pygame.mouse.get_pos()
            crosshair_width, crosshair_height = engine.crosshair.get_size()
            crosshair_postion = (mouse_x - (crosshair_width / 2), mouse_y - (crosshair_height / 2))
                
                
            ## gameplay logics
            spaceship.move_spaceship((move_x, move_y))
            spaceship.calculate_angle_by_mouse(pygame.mouse.get_pos())
            
            ## asteroids logics
            for asteroid in asteroids[:]: 
                asteroid.set_y(asteroid.get_y() + difficulty) 
                
                ## shoots lasers colisions
                for laser in lasers[:]:
                    if asteroid.verify_laser_colision(laser):
                        asteroids.remove(asteroid)
                        lasers.remove(laser)
                        pygame.mixer.Sound.play(engine.explosion)
                        points += 1
                        break
                        
                ## asteroids colisions
                if spaceship.verify_colision(asteroid):
                    pygame.mixer.Sound.play(engine.explosion)
                    writeData(nick_name, points)
                    game_over()
            
            
            ## write points infos 
            text_points = engine.font.render("Pontos: " + str(points), True, engine.yellow)
            text_points_width = (text_points.get_size()[0]) + 60
            
            text_pause = engine.font_small.render("Press Space to Pause Game", True, engine.yellow)
            text_pause_width = (text_points.get_size()[0])
            
            label_width = text_points_width + text_pause_width + 52
            label_point = pygame.Surface((label_width, 35), pygame.SRCALPHA)
            pygame.draw.rect(label_point, engine.black_transparent_2, (0, 0, label_width, 35))
            
            
            ## draw
            engine.window.fill(engine.white)    
            engine.window.blit(engine.background, (0, 0))
            engine.window.blit(spaceship.sprite, spaceship.rect)
            
            for laser in lasers[:]:
                laser.update()
                laser.draw(engine.window)

                if not (0 <= laser.x <= engine.game_resolution[0] and 0 <= laser.y <= engine.game_resolution[1]):
                    lasers.remove(laser)
            
            for asteroid in asteroids:
                engine.window.blit(asteroid.sprite, asteroid.rect)
                
            engine.window.blit(label_point, (5, 11))
            engine.window.blit(text_points, (15,15))
            engine.window.blit(text_pause, (text_points_width, 25))
            engine.window.blit(engine.crosshair, crosshair_postion)
                
        
        pygame.display.flip()
        engine.clock.tick(engine.clock_tick)
        

def ajust_str(s, max_len, space):
    if (len(str(s)) < max_len):
        return str(s).ljust(max_len + space)
    else:
        return str(s)[:max_len].ljust(max_len + space)

        
def game_over():
    engine.change_music("imperial_march")
    placar_font = pygame.font.SysFont("Courier New", 20)
    
    engine.window.fill(engine.white)  
    engine.window.blit(engine.endgame_background, (0, 0))
    
    for i in range(1, 4):
        engine.window.blit(engine.filter_transparent, (0, 0))
        
    
    box_center_x = engine.game_resolution[0] / 2
    text_spacing = 50
    
    
    table = placar_font.render(f"Pontos    Nickname       Data                     ", True, engine.white)
    table_width , table_height = table.get_size()
    table_x= box_center_x - (table_width / 2)
    table_y = text_spacing * 3
    engine.window.blit(table, (table_x, table_y))
    
    
    data = getData()
    for i in range(0, 5):
        if len(data) >= i + 1:
            points = ajust_str(data[i][1], 5, 5)
            nick = ajust_str(data[i][0], 10, 5)
            date = ajust_str(data[i][2], 20, 5)
            
            regTxt = placar_font.render(f"{points}{nick}{date}", True, engine.white)
            regTxt_x= table_x
            regTxt_y = (text_spacing * (i+1)) + table_y
            engine.window.blit(regTxt, (regTxt_x, regTxt_y))

        
        
    goto_to_menu_txt = engine.font.render("Voltar ao menu", True, engine.black)
    goto_to_menu_width , goto_to_menu_height = goto_to_menu_txt.get_size()
    goto_to_menu_x = box_center_x - (goto_to_menu_width / 2)
    goto_to_menu_y = regTxt_y + (text_spacing * 3)
    
    goto_to_menu_box_width = goto_to_menu_width + 100
    goto_to_menu_box_height = goto_to_menu_height + 20
    goto_to_menu_box_x = box_center_x - (goto_to_menu_box_width / 2)
    goto_to_menu_boxr_y = goto_to_menu_y - 10


    goto_menu_button = None
    
    pygame.mouse.set_visible(True)
    while True:
        
        goto_menu_button = pygame.draw.rect(engine.window, engine.white, (goto_to_menu_box_x, goto_to_menu_boxr_y, goto_to_menu_box_width, goto_to_menu_box_height), border_radius=15)
        engine.window.blit(goto_to_menu_txt, (goto_to_menu_x, goto_to_menu_y))
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
                
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if goto_menu_button.collidepoint(evento.pos):
                    goto_to_menu_box_width -= 10
                    goto_to_menu_box_height -= 5

                
            elif evento.type == pygame.MOUSEBUTTONUP:
                if goto_menu_button.collidepoint(evento.pos):
                    goto_to_menu_box_width += 10
                    goto_to_menu_box_height += 5
                    menu(engine.home_background)
        
        pygame.display.flip()
       