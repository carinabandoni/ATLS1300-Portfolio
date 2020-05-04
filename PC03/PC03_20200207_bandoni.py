#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 11:03:02 2020

@author: carinabandoni
"""


# PC03 - Generative Art
# Bandoni
# 2/7/20
# 
# This code animates abstract lines going outwards
#==========================


from turtle import * 
from random import *
import random

screen = Screen()
pete = Turtle()

pete.color("pink")


##this creates the multi colored shapes in pink shades
for n in range(50):
    pensize(5)
    pencolor("pink")
    speed(200)
    goto(random.randint(-200, 200), random.randint(-200, 200))
    pendown()
    pete.showturtle()
    pensize(2)
    pencolor("hotpink") #color change
    forward(100)
    right(90)
    forward(100)
    pensize(2) 
    home()

##this creates the multi colored shapes in blue shades
for n in range(60):
    pensize(5)
    pencolor("skyblue")
    goto(random.randint(-400, 400), random.randint(-400, 400))
    pendown()
    pete.showturtle()
    pencolor("royalblue") ##changes color
    forward(100)
    right(90)
    forward(100)
    home()    

done()



