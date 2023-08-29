import pygame
import game_settings as gs
from pygame.math import Vector2 as v2

class Player(pygame.sprite.Sprite):
    def __init__(self, position, group, obstacle_sprites) -> None:
        super().__init__(group)
        self.image = pygame.image.load("graphix/test/player.png").convert_alpha()
        image_size = pygame.math.Vector2(self.image.get_size()) * 3
        scaled_image = pygame.transform.scale(self.image, (image_size))
        self.image = scaled_image
        # scaled_img muss wieder auf self.image gesetzt werden, sonst keine Skalierung
        self.rect = self.image.get_rect(topleft = position)
        self.hitbox = self.rect.inflate(-40, -32)
        
        self.obstacle_sprites = obstacle_sprites
        
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
            
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            
        # horizontal movement + collision
        self.hitbox.x += self.direction.x * speed
        self.check_collision("horizontal")
        # vertical movement + collision
        self.hitbox.y += self.direction.y * speed
        self.check_collision("vertical")
        self.rect.center = self.hitbox.center
        
    def check_collision(self, axis):
        for sprite in self.obstacle_sprites.sprites():
            if axis == "horizontal":
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
                    #self.position.x = self.hitbox.centerx
            else:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
                    #self.position.y = self.hitbox.centery
        
    def update(self):
        self.handle_inputs()
        self.move(self.speed)