import pygame
from destiny.constants import*
from destiny.board import*
from destiny.buttons import*

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Destiny Board Game')

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
    
        board.draw_squares(WIN)
        pygame.display.update()

        # Draw the add unit button to the right
        pygame.draw.rect(WIN, BUTTON_COLOR, (450, 50, 100, 50))
        button_text = FONT.render("Add Unit", True, BLACK)
        WIN.blit(button_text, (460, 60))


    pygame.quit()

main()