import sys
import pygame

class AlienInvasion:

    def __init__(self):
        #initialize the game
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")


    def run_game(self):
        #start the main loop of the game
        while True:
            #keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #most recent screen visibility
            pygame.display.flip()

if __name__ == '__main__':
    #main method, initiate and run the game
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()

