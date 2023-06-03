from enum import Enum

import pygame


class Directions(Enum):
    Up = 0,
    Down = 1,


class Paddle:
    def __init__(self, screen,position):
        self.screen = screen
        self.radius = 10
        self.speed = 10
        self.direction = Directions.Up.name
        self.color = (250, 200, 17)
        self.rect = pygame.Rect(position, 250, 15, 100)

    def draw(self):  # Alterar este desenho
        pygame.draw.rect(self.screen, self.color,self.rect)

    def move(self,keyUp,keyDown):
        key = pygame.key.get_pressed()

        if key[keyUp] and self.rect.y - self.speed > 0:
            self.rect.y -= self.speed
        if key[keyDown] and self.rect.y + self.rect.height + self.speed < self.screen.get_height():
            self.rect.y += self.speed
