import pygame
from pygame.sprite import Sprite
import game_settings as gs
from tile import Tile
from player import Player

class Level:
    def __init__(self, screen) -> None:
        
        # get display surface
        self.display_surface = screen
        
        # Sprite Group Setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        
        # Sprite Setup
        self.create_map()
    
    def create_map(self):
        for row_index, row in enumerate(gs.WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * gs.TILESIZE
                y = row_index * gs.TILESIZE
                if col == "x":
                    Tile((x,y),[self.visible_sprites, self.obstacle_sprites])
                if col == "p":
                    self.player = Player((x,y),[self.visible_sprites], self.obstacle_sprites)
                    # hier später noch einmal checken
    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
    
    # Order sprites by Y coordinate and setting the camera position
    def custom_draw(self, player):
        
        # get offset position
        self.offset.x = player.rect.centerx - gs.WIDTH // 2
        self.offset.y = player.rect.centery - gs.HEIGHT // 2

        # draw all sprites ordered by Y coordinate
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_position)