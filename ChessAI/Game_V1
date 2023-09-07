import pygame
from Const import *


class Game:
    def __init__(self):
        pass

    def bg(self, sur):
        for row in range(Rows):
            for col in range(Cols):
                if (row + col) % 2 == 0:
                    colour = (245,222,179)
                else:
                    colour = (255,248,220)

                rect = (col * SqSize, row * SqSize, SqSize, SqSize)

                pygame.draw.rect(sur, colour, rect)
