import pygame

class Level:
    def __init__(self) -> None:
        
        # Sprite Group Setup
        self.all_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

    def run(self):
        # update and draw the game
        pass