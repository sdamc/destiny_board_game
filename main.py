# main.py
import pygame
from destiny.constants import *
from destiny.board import *
from destiny.buttons import *
from destiny.units import create_unit

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Destiny Board Game')

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    
    capturing_input = False  # Flag to control when to capture input
    unit_stats = None  # Initialize unit_stats

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 950 <= event.pos[0] <= 1050 and 50 <= event.pos[1] <= 100:
                    capturing_input = True  # Set the flag to start capturing input

        if capturing_input:
            unit_stats = get_stats_input(["Name:", "Strength:", "Agility:", "HP:", "Field Position:"], WIN)
            print("Input Stats:", unit_stats)
            
            # Check if unit_stats is not None before attempting to create a unit
            if unit_stats is not None:
                unit = create_unit(unit_stats)
                if unit is not None:
                    print("Created Unit:", unit.__dict__)
            
            capturing_input = False  # Reset the flag after capturing input

        board.draw_squares(WIN)

        # Draw the add unit button to the right
        pygame.draw.rect(WIN, BUTTON_COLOR, (950, 50, 100, 50))
        button_text = FONT.render("Add Unit", True, BLACK)
        WIN.blit(button_text, (960, 60))

        pygame.display.update()

    pygame.quit()

main()
