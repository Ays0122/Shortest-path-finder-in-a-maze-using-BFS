from collections import deque
import pygame
import sys
import math
from examplemazes import get_user_input

pygame.init()

# Maze (0 = open path, 1 = wall)

maze=get_user_input()

start = (0, 0)  # Top-left corner
end = (24, 24)    # Bottom-right corner


def start_position(r,c):
    global start
    start = (r,c)
    return start
def end_position(r,c):
    global end
    end = (r,c)
    return end

def print_maze(maze):
    for row in maze:
        print(" ".join(map(str, row)))

def draw_text(text, font, text_col):
    img = font.render(text, True, text_col)
    screen.blit(img, (int(width/2)-110, int(height/2)-50))
    pygame.display.update()
    pygame.time.delay(1500)

def maze_solver(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    moves = [(0,1), (1,0), (0,-1), (-1,0)] #Valid move set
    queue = deque([ ( start[0], start[1], [] ) ]) #(row, col, path taken)
    visited = set([start])

    while queue:
        r, c, path = queue.popleft()
        path = path + [(r,c)] #Store path

        if (r,c) == end:
            return path #Gives the path after reaching end

        # Moving in available direction(up down left right)
        for dr, dc in moves:
            nr = r + dr
            nc = c + dc
            # Check for valid moves
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0 and (nr, nc) not in visited:
                queue.append((nr, nc, path))
                visited.add((nr, nc))
                draw_processing_path(maze, nr, nc)
    return 0

#Graphical stuffs
RED = (255, 0, 0)
#WHITE = (255,255,255)
#BLACK = (0 ,0, 0)
BLUE = (0, 0, 255)
#GREEN = (0, 255, 0)
#LIGHT_PURPLE = (209, 129, 249)
ORANGE = (255, 165, 0)
text_font = pygame.font.SysFont("Arial", 30, bold=True)
CELL_SIZE = 20
width = height = CELL_SIZE*len(maze)
size = (width, height)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Textures
image_block = pygame.image.load('textures/wood_block.png')
image_block = pygame.transform.scale(image_block, (CELL_SIZE, CELL_SIZE))
image_patch = pygame.image.load('textures/wood_texture.png')
image_patch = pygame.transform.scale(image_patch, (CELL_SIZE, CELL_SIZE))
image_path_checked = pygame.image.load('textures/wood_texture_plorp.png')
image_path_checked = pygame.transform.scale(image_path_checked, (CELL_SIZE, CELL_SIZE))
image_final_path = pygame.image.load('textures/wood_texture_green.png')
image_final_path = pygame.transform.scale(image_final_path, (CELL_SIZE, CELL_SIZE))

def draw_maze(maze):
    rows = len(maze)
    cols = len(maze[0])

    for r in range(rows):
        for c in range(cols):

            if maze[r][c] == 1:
                screen.blit(image_block, (c*CELL_SIZE,r*CELL_SIZE))
                #pygame.draw.rect(screen, BLACK, (c*CELL_SIZE,r*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif maze[r][c]==0:
                screen.blit(image_patch, (c * CELL_SIZE, r * CELL_SIZE))
                #pygame.draw.rect(screen, WHITE, (c*CELL_SIZE, r*CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_processing_path(maze, r, c):
    screen.blit(image_path_checked, (c * CELL_SIZE, r * CELL_SIZE))
    #pygame.draw.rect(screen, LIGHT_PURPLE, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()
    clock.tick(60)


def draw_shortest_path(maze):
    reset=False
    path=maze_solver(maze, start, end)
    if path == 0:
        draw_text("NO VALID PATH", text_font, RED)

    else:
        for r,c in path:
            screen.blit(image_final_path, (c*CELL_SIZE, r*CELL_SIZE))
            #pygame.draw.rect(screen, GREEN, (c*CELL_SIZE, r*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.display.update()
            clock.tick(120)
        while not reset:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return



run = True
start_selection = True
pygame.display.set_caption('Shortest Path Maze Solver Using BFS')

#Game starts
while run:
    for event in pygame.event.get():
        draw_maze(maze)
        #draw start and end point
        (s_r, s_c) = start
        (e_r, e_c) = end
        pygame.draw.rect(screen, BLUE, (s_c * CELL_SIZE, s_r * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, ORANGE, ((e_c) * CELL_SIZE, (e_r) * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.update()
        if event.type == pygame.QUIT:
            #np.save("maze.npy", maze)
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = event.pos[0]
            posy = event.pos[1]
            r = int(math.floor(posy / CELL_SIZE))
            c = int(math.floor(posx / CELL_SIZE))
            print(f"start={start} end={end}")
            print(f"r={r} c={c}")
            if event.button==2: #middle click

                draw_shortest_path(maze)
                pygame.display.update()
            if event.button==1: #left click
                if start!=(r,c) and end != (r,c) and maze[r][c]==0:
                    maze[r][c]=1
                    screen.blit(image_block, (c * CELL_SIZE, r * CELL_SIZE))
                    #pygame.draw.rect(screen, BLACK, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))

                    pygame.display.update()
                elif maze[r][c]==1:
                    maze[r][c]=0
                    screen.blit(image_patch, (c * CELL_SIZE, r * CELL_SIZE))
                    #pygame.draw.rect(screen, WHITE, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    pygame.display.update()

            if event.button==3:  #right click
                if start_selection:
                    start_position(r,c)
                    start_selection=False
                else:
                    end_position(r,c)
                    start_selection=True
print(maze)




