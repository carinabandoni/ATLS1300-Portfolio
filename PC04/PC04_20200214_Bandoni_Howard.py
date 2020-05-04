#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 11:08:57 2020
PSEUDOCODE:
    arrow keys move rectange
    return key changes color of rectangle
    space bar key changes color of rectange
@author: carinabandoni
"""
# PC04 - Interactive Robot
# Bandoni and Howard
# 2/18/20
# 
# This code animates a robot
#==========================


import pygame
from random import *
import time


pygame.init() 
screen = pygame.display.set_mode((500,500))

screen.fill((186, 246, 255 )) #background color


pete = 0
Run = True
x = randint(40,50)
y = 50


speed = 10 
scale = 5 
color = (75, 241, 224)

#GAME LOOP
while Run:
    time.sleep(.1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            Run = False
    
## DR. Z code down below from class 2-13-20 
    keys = pygame.key.get_pressed() 
    if keys [pygame.K_RIGHT]:

        x += speed 
    if keys [pygame.K_LEFT]:
        x -= speed 

    if keys [pygame.K_UP]:
        y -= speed 

    if keys [pygame.K_DOWN]:
        y += speed 
        
    if keys [pygame.K_SPACE]:
        color = (33,97,140)
## end of code from class
    if keys [pygame.K_RETURN]:
        color = (164, 243, 254 )
    
        
    #fills screen 
    screen.fill((255,186,250))
    
    Rect = pygame.draw.circle(screen, (110, 90, 253 ), (250, 250), 50, 3)
    Rect = pygame.draw.rect(screen,color,(x,y,30,50)) #moving piece
    x += randint(-3,5)
    pygame.display.update()
    ## jiggleing on perpose!!!
    
    stop = randint(300,500)
    if x > stop:
        Run = False # stops animation



pygame.quit()
