import pygame as pg
from random import randint
import time
pg.mixer.pre_init(44100, -16, 2, 2048)

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Purple Rain')
clock = pg.time.Clock()

def draw_text(text, color, surface, x, y, size = 32, alpha = 255, origin = "center"):
    font = pg.font.SysFont("Monocraft", size)
    textobj = font.render(str(text), True, color)
    textobj.set_alpha(alpha)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def display_fps(clock):
    screen = pg.display.get_surface()  
    font = pg.font.SysFont("Monocraft", 32)
    textobj = font.render(str(int(clock.get_fps())), True, (255, 255, 255))
    textobj.set_alpha(255)
    textrect = textobj.get_rect()
    textrect.topleft = (20, 20)
    screen.blit(textobj, textrect)
	#draw_text(str(int(clock.get_fps())),(255, 255, 255), screen, 20, 20)

def remap(x, oMin, oMax, nMin, nMax ):

#range check
    if oMin == oMax:
        return None

    if nMin == nMax:
        return None

    #check reversed input range
    reverseInput = False
    oldMin = min( oMin, oMax )
    oldMax = max( oMin, oMax )
    if not oldMin == oMin:
        reverseInput = True

    #check reversed output range
    reverseOutput = False   
    newMin = min( nMin, nMax )
    newMax = max( nMin, nMax )
    if not newMin == nMin :
        reverseOutput = True

    portion = (x-oldMin)*(newMax-newMin)/(oldMax-oldMin)
    if reverseInput:
        portion = (oldMax-x)*(newMax-newMin)/(oldMax-oldMin)

    result = portion + newMin
    if reverseOutput:
        result = newMax - portion

    return result

