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
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirx = 0
        self.diry = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirx = -1
                    self.diry = 0
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

                elif keys[pygame.K_RIGHT]:
                    self.dirx = 1
                    self.diry = 0
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

                elif keys[pygame.K_UP]:
                    self.dirx = 0
                    self.diry = -1
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

                elif keys[pygame.K_DOWN]:
                    self.dirx = 0
                    self.diry = 1
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]
            for i , c in enumerate(self.turns):
                p= c.pos[:i]
                if p in self.turns:
                    turn = self.turns[p]
                    c.move(turn[0], turn[1])
                    if i == len(self.body)-1:
                        self.turns.pop(p)
                else:
                    if c.dirx == -1 and c.pos [0] <=0: c.pos = (c.rows-1, c.pos[1])
                    elif c.dirx == 1 and c.pos [0] >=0 c.rows-1: c.pos = (0,c.rows-1, c.pos[1])

    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.dirx = 0
        self.diry = 1
        self.turns = {}

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirx, tail.diry

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1] + 1)))

    def draw(self, surface):
        pass

def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x=0
    y=0
    for l in range(rows):
        x= x+ sizeBtwn
        y= y+ sizeBtwn

        pygame.draw.line(surface, (255,255,255),(x,0),(x,w))
        pygame.draw.line(surface, (255,255,255),(0,y),(w,y))
    

def redrawWindow(surface):
    global rows, width
    surface.fill(0,0,0)
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