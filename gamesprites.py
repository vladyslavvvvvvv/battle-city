import pygame
from abc import ABC, abstractmethod


class GameSprite(ABC, pygame.sprite.Sprite):
    def __init__(self, image_filename:str, coords=tuple([int, int]),size=tuple([int,int])):
        self.image = pygame.transform.scale(
                        pygame.image.load(image_filename),
                        size    )