"""
maze_structure = [
        "XXXXX  X",
        "XP     X",
        "XXXXX  X"
    ]
"""
import pygame


class Maze:

    def __init__(self, screen_width, screen_height, maze_structure, screen):
        self.screen = screen
        self.maze_structure = maze_structure
        self.block_width = screen_width / len(maze_structure[0])
        self.block_height = screen_height / len(maze_structure)
        self.blocks = []
        self.__create_bloco()

    def __create_bloco(self):
        for i in range(len(self.maze_structure)):
            for j in range(len(self.maze_structure[0])):
                if self.maze_structure[i][j] == "X":
                    rect = pygame.Rect(self.block_width * j, self.block_height * i, self.block_width, self.block_height)
                    self.blocks.append(rect)

    def draw(self):
        for block in self.blocks:
            pygame.draw.rect(self.screen, (101, 20, 200), rect=block)
