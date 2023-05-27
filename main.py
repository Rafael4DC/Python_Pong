import pygame

from maze import Maze
from paddle import Paddle

pygame.init()

width = 1000
height = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")
PackmaIcon = pygame.image.load("images/packmaImg.png")
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
pacman = Paddle(screen)

running = True
while running:
    pacman.move()
    screen.fill(background_color)
    pacman.draw()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
