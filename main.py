#Snake Game
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox 


class cube(object):
    rows=0
    w=0
    def __init__(self, start, dirx=1, diry=0, color=(255,0,0)):
        pass

    def move(self, dirx, diry):
        pass

    def draw(self, surface, eyes=False):
        pass

class snake(object):
    def __init__(self,color, pos):
        pass
    def move(self):
        pass
    def reset(self, pos):
        pass
    def addCube(self):
        pass
    def draw(self, surface):
        pass

def drawGrid(w, rows, surfaces):
    sizeBtwn = w // rows

    x=0
    y=0
    for l in range(rows):
        x= x+ sizeBtwn
        y= y+ sizeBtwn
    

def redrawWindow(surface):
    global rows, width
    win.fill(0,0,0)
    drawGrid(width, rows, surface )
    pygame.display.update()


def randomSnack(rows, items):
    pass

def message_box(subject, content):
    pass


def main():
    global width, rows
    width = 500
    height = 500
    rows= 20
    win= pygame.display.set_mode((width, width))
    s= snake((255,0,0), (10,10))

    flag= True

    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50)
        clock.tick(10) #our snake will move 10 block in seconds
        redrawWindow(win)

    pass

rows= 0
w= 0
h= 0
cube.rows =rows
cube.w= w

main()