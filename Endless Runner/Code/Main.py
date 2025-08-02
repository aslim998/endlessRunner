#Modules
import pygame, sys, time, Sprites
from Settings import *
#Game
class Game:
    def __init__ (self):
        pygame.init()
        pygame.display.set_caption(Title)
        self.Player = Sprites.Player(allSprites)
    def Main(self):
        #self.loadSpritesheet()
        global Run, Clock, FPS
        self.lastTime = time.time()
        Clock.tick(FPS)
        while Run:
            self.deltaTime = time.time() - self.lastTime
            self.lastTime = time.time()
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:
                    Run = False
                    pygame.quit()
                    sys.exit()
            #Draws
            Screen.fill('black')
            allSprites.draw(Screen)
            #Logics
            allSprites.update(self.deltaTime)
            Clock.tick(FPS)
            pygame.display.flip()
    
if __name__ == "__main__":
    Gameplay = Game()
    Gameplay.Main()