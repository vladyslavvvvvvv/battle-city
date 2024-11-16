import pygame
im

WIDTH = 1200
HEIGHT = 600
FPS = 60


class Game:
    def __init__(self,background_filename=None):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.clock()

        if background_filename is not None:
            self.background = pygame.transform.scale(
                                pygame.image.load(background_filename), 
                                (WIDTH,HEIGHT))
            
        def run(self):
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                
                pygame.display.flip()
                self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()