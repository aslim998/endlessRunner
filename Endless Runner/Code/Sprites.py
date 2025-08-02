#Modules
import pygame
from Settings import *
#Sprites
class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = img.load('Assets/Graphics/MaskDude/run.png')
        self.rect = self.image.get_rect()
        self.Sprites = [img.load('Assets/Graphics/MaskDude/run.png').convert_alpha(), img.load('Assets/Graphics/MaskDude/jump.png').convert_alpha(), img.load('Assets/Graphics/MaskDude/idle.png').convert_alpha(), img.load('Assets/Graphics/MaskDude/fall.png').convert_alpha()]
        self.SpriteSheetIndex = 0
        self.SpriteSheet = self.Sprites[self.SpriteSheetIndex]
        self.numFrames = (12, 1, 11, 1)
        self.frameDimensions = (32, 32)
        self.IDX = 0
    def loadSpritesheet(self):
        self.Frames = []
        for i in range(self.numFrames[self.SpriteSheetIndex]):
            Frame = self.SpriteSheet.subsurface(pygame.Rect(
                i*self.frameDimensions[0], 
                0,
                self.frameDimensions[0], 
                self.frameDimensions[1]))
            self.Frames.append(Frame)
    def Animate(self, dt):
            if self.IDX >= len(self.Frames)-dt*10: self.IDX = 0
            self.IDX += dt*10
            self.image = self.Frames[int(self.IDX)]
    def update(self, dt):
        self.rect = self.image.get_rect()
        self.loadSpritesheet()
        self.Animate(dt)