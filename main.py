import pygame

from maze import Maze
from paddle import Paddle

pygame.init()

width = 1000
height = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")
PackmaIcon = pygame.image.load("images/estre.png")
pygame.display.set_icon(PackmaIcon)

background_color = (211, 167, 219)
maze_structure = [
    "        ",
    "        ",
    "        ",
    "XP     X",
    "XXXXX  X"
]
maze = Maze(width, height, maze_structure, screen)
paddleL = Paddle(screen,20)
paddleR = Paddle(screen,970)
running = True
while running:
    paddleL.move(pygame.K_w,pygame.K_s)
    paddleR.move(pygame.K_UP, pygame.K_DOWN)
    screen.fill(background_color)
    paddleL.draw()
    paddleR.draw()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
