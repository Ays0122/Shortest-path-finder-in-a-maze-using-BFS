# examplemazes.py
import pygame
import numpy as np
import sys

pygame.init()
pygame.display.set_caption('Options')

maze0=np.zeros((25,25))
maze1=np.load("maze1.npy")
maze2=np.load("maze2.npy")
maze3=np.load("maze2.npy")
def get_user_input():
    # Graphical stuffs
    RED = (255, 0, 0)
    color_dark = (100, 100, 100)
    color_light = (175, 175, 175)

    width = 215
    height = 215
    size = (width, height)
    screen = pygame.display.set_mode(size)

    text_font = pygame.font.SysFont("Arial", 20, bold=True)

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    run = True

    screen.fill(color_light)

    for r in range(3):
        row_line = pygame.Rect((0, 0 + 105 * r, width, 5))
        pygame.draw.rect(screen, color_dark, row_line)

    for c in range(3):
        row_line = pygame.Rect((0 + 105 * c, 0, 5, height))
        pygame.draw.rect(screen, color_dark, row_line)

    draw_text("Custom", text_font, RED, 5 + 15, 5 + 42)
    draw_text("Maze 1", text_font, RED, 10 + 115, 5 + 42)
    draw_text("Maze 2", text_font, RED, 5 + 12, 20 + 125)
    draw_text("Maze 3", text_font, RED, 10 + 115, 20 + 125)

    pygame.display.update()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 5<=mouse[0]<105 and 5<=mouse[1]<=105:
                    return maze0

                elif 110<=mouse[0]<210 and 5<=mouse[1]<=105:
                     return maze1

                elif 5<=mouse[0]<105 and 110<=mouse[1]<210:
                     return maze2

                elif 110<=mouse[0]<210 and 110<=mouse[1]<210:
                     return maze3

                run = False

