#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:54:32 2020

@author: carinabandoni
"""
# PC08 - SoundWave
# Bandoni and Howard
# 3/21/20
#
# Psudocode Below
#==========================
#This code is meant to create sound waves that will eventually move to audio
#Top of screen is blue, wave represents ocean wave
#yellow bottom box is meant to be sand
#yellow circle follows wave
#yellow circle in corner represents sun and gets bigger and smaller as it radiates
#wave will move repeatedly in a loop
#=====================================

import pygame
import time
import math
from random import *

canvas_width = 640
money = (255,212,0)
canvas_height = 480

x = 0
y = 0
r = 60
t = 10
v = 10


color = pygame.Color(255, 255,255, 0)
background_color = pygame.Color(92, 122, 245, 0)
pygame.init()

screen = pygame.display.set_mode((canvas_width, canvas_height))
screen.fill(background_color)
surface = pygame.Surface((canvas_width, canvas_height))
surface.fill(background_color)
running = True
m = 80

#first function which is the sun
def circlegrowing():
    global m
    if m < 90:
        m += 1
        pygame.draw.circle(screen,money,(t,v),m)
        time.sleep(0.006)
    elif m >= 90:
        m -= 45
        circCol = (randint(100,255),randint(100,255),randint(100,255))
        pygame.draw.circle(screen,money,(t,v),m)

#second function which is the wave moving across the screen
def wave2():
  returnList = []
  for x in range(0, canvas_width):
        y = int((canvas_height/2) + amplitude*math.sin(frequency*((float(x/canvas_width)*(2*math.pi) + (speed*time.time())))))
        returnList.append(y)
        surface.set_at((x, y), color)
  return returnList

# def wave():
#    frequency = 4
#    amplitude = 50
#    speed = 1
#    for i in range(0, w):
#        f = int((h/2) + amplitude*math.sin(frequency*((float(i)/w)*(2*math.pi) + (speed*time.time()))))
#        surface.set_at((i, f), circCol)
#    screen.blit(surface, (0, 0))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    surface.fill(background_color)
    # wave()
    frequency = 2
    amplitude = 50
    speed = 1
    ys = wave2()
    screen.blit(surface, (0, 0))
    pygame.draw.rect(screen, (240, 242, 166,), (0, 290, 680, 250)) #makes the size of yellow square
    pygame.draw.circle(screen, money, (x, ys[0]), r)
    pygame.draw.circle(screen, money, (t, v), m)
    circlegrowing()
    
    pygame.display.flip()

# this is my source with the wave code- https://ericeastwood.com/blog/7/animated-sine-wave-two-ways-with-pygame-and-tkinter
    
