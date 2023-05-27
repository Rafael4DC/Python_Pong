from enum import Enum

import pygame


class Directions(Enum):
    Up = 0,
    Down = 1,


class Paddle:
    def __init__(self, screen):
        self.screen = screen
        self.radius = 10
        self.speed = 10
        self.direction = Directions.Up.name
        self.color = (250, 200, 17)
        self.rect = pygame.Rect(20, 250, 15, 100)

    def draw(self):  # Alterar este desenho
        pygame.draw.rect(self.screen, self.color,self.rect)

    def move(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_UP]:
            self.rect.y -= self.speed
        if key[pygame.K_DOWN]:
            self.rect.y += self.speed
