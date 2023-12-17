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
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 950 <= event.pos[0] <= 1050 and 50 <= event.pos[1] <= 100:
                    unit_name = get_user_input("Enter Unit Name:")
                    print("Unit Name:", unit_name)
    
        board.draw_squares(WIN)
        

        # Draw the add unit button to the right
        pygame.draw.rect(WIN, BUTTON_COLOR, (950, 50, 100, 50))
        button_text = FONT.render("Add Unit", True, BLACK)
        WIN.blit(button_text, (960, 60))

        input_box = pygame.Rect(950, 150, 140, 32)
        color_inactive = pygame.Color('lightskyblue3')

        pygame.display.update()


    pygame.quit()

main()