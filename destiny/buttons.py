import pygame
import sys

def get_user_input(prompt, default_value=""):
    input_box = pygame.Rect(200, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = default_value
    input_active = True

    # Label above the input box
    label_text = label_font.render(prompt, True, BLACK)

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

        window.fill(RED)
        
        window.blit(label_text, (200, 70))

        txt_surface = FONT.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        window.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(window, color, input_box, 2)

        pygame.display.flip()
        

    return text
