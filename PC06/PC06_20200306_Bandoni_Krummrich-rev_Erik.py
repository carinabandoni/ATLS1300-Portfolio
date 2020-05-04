#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 11:01:30 2020

@author: erikkrummrich

its makes waves and shit
"""

from turtle import *
import numpy as np
from random import *
randomColor = (randint(0,255)/255.0,randint(0,255)/255.0,randint(0,255)/255.0,)
randomColors = (randint(0,255)/255.0,randint(0,255)/255.0,randint(0,255)/255.0,)
pen = Turtle()
marker = Turtle()
disp = Screen()
disp.reset()
pen.color(randomColor)
marker.color(randomColors)
#math can be coool I just was sick of shapes. 
disp.setworldcoordinates(0,-1.5,360,1.5) #changes where the line starts
x = randint(-4,4)
z = randint(-6,6)
#fillList = [(0,30,45,60,90,120,150,180]
def drawlines():
    
    for angle in range(360):
        y = np.sin(np.radians(angle*x)) #calling the lines
        pen.goto(angle,y)   
    #sin waves for a more original art. Everyone else lowkey kncocked off dr Z 
        
    for angle in range(360):
        t = np.cos(np.radians(angle*z))
        marker.goto(angle,t)
# one wave is not cool to look at really need and if = 0 dont graph 
    
drawlines()

disp.update()
    

     
