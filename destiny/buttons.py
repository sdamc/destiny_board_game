import pygame
import sys
from .constants import*

def get_user_input(prompt, default_value=""):
    input_box = pygame.Rect(950, 150, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = default_value
    input_active = True

    # Label above the input box
    label_text = LABEL_FONT.render(prompt, True, BLACK)

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        
        txt_surface = FONT.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width        
        

    return text
