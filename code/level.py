import pygame
import game_settings as gs
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self, screen) -> None:
        
        # get display surface
        self.display_surface = screen
        
        # Sprite Group Setup
        self.all_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        
        # Sprite Setup
        self.create_map()
    
    def create_map(self):
        for row_index, row in enumerate(gs.WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * gs.TILESIZE
                y = row_index * gs.TILESIZE
                if col == "x":
                    Tile((x,y),[self.all_sprites, self.obstacle_sprites])
                if col == "p":
                    self.player = Player((x,y),[self.all_sprites])

    def run(self):
        # update and draw the game
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update()
        debug(self.player.direction)