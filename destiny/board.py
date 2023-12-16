import pygame
from .constants import*

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.whitekings = 0

    def draw_squares(self, win):
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range (COLS):
                pygame.draw.rect(win, BLACK, (row *SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
