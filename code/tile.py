import pygame
import game_settings as gs

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, group) -> None:
        super().__init__(group)
        self.image = pygame.image.load("graphix/test/rock.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = position)
        self.hitbox = self.rect.inflate(0, -16)