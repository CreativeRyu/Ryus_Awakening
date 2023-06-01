import pygame
import game_settings as gs
from pygame.math import Vector2 as v2

class Player(pygame.sprite.Sprite):
    def __init__(self, position, group) -> None:
        super().__init__(group)
        self.image = pygame.image.load("graphix/test/player.png").convert_alpha()
        image_size = pygame.math.Vector2(self.image.get_size()) * 3
        scaled_image = pygame.transform.scale(self.image, (image_size))
        self.image = scaled_image 
        # scaledimg muss wieder auf self.image gesetzt werden, sonst keine Skalierung
        self.rect = self.image.get_rect(topleft = position)
        
        # float based movement
        self.direction = v2()
        self.speed = 5
        
    def handle_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else: 
            self.direction.y = 0
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else: 
            self.direction.x = 0
            
    def move(self):
        self.rect.center += self.direction * self.speed
        
    def update(self):
        self.handle_inputs()
        self.move()