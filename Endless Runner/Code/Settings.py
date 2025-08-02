#Modules
import pygame
from pygame import image as img
from pygame.image import load as load
from os import path as pth
#Settings
pygame.init()
pygame.font.init()
Dimensions = (800, 400)  # Width, Height
WIDTH = Dimensions[0]
HEIGHT = Dimensions[1]
FPS = 60
Screen = pygame.display.set_mode(Dimensions)
Title = "Breakout"
Run = True
Clock = pygame.time.Clock()
allSprites = pygame.sprite.Group()
collisionSprites = pygame.sprite.Group()