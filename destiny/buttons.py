# buttons.py
import pygame
import sys
from .constants import *

def get_stats_input(prompts, win):
    input_boxes = [pygame.Rect(200, 100 + i * 40, 140, 32) for i in range(len(prompts))]
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text_values = [""] * len(prompts)
    input_active = True

    # Labels above the input boxes
    label_texts = [LABEL_FONT.render(prompt, True, BLACK) for prompt in prompts]

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, box in enumerate(input_boxes):
                    if box.collidepoint(event.pos):
                        active = not active
                        color = color_active if active else color_inactive
                    else:
                        active = False
                        color = color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        text_values[i] = text_values[i][:-1]
                    else:
                        text_values[i] += event.unicode

        win.fill(RED)  # Filling the window with a color to clear the previous input box positions

        for i, box in enumerate(input_boxes):
            label_rect = label_texts[i].get_rect(center=(box.x + box.w / 3, box.y + 20))
            win.blit(label_texts[i], label_rect)

            txt_surface = FONT.render(text_values[i], True, color)
            width = max(200, txt_surface.get_width() + 10)
            box.w = width
            win.blit(txt_surface, (box.x + 5, box.y + 5))
            pygame.draw.rect(win, color, box, 2)

        pygame.display.flip()

    return {prompt: text for prompt, text in zip(prompts, text_values)}
