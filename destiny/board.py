import pygame
from .constants import *

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        

    def draw_squares(self, win):
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(COLS):
                square_rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(win, WHITE, square_rect)
                pygame.draw.rect(win, BLACK, square_rect, 1)

