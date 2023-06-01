import pygame
import sys
import game_settings as gs
from level import Level

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.game_screen = pygame.display.set_mode((gs.WIDTH, gs.HEIGHT))
        pygame.display.set_caption("Ryu's Awakening")
        self.game_clock = pygame.time.Clock()
    
    def execute_gameloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.game_screen.fill("black")
            pygame.display.update()
            self.game_clock.tick(gs.FPS)

if __name__ == "__main__":
    game = Game()
    game.execute_gameloop()