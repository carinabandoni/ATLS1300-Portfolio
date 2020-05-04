#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:09:52 2020

@author: carinabandoni
"""

# PC02 - Animating with Turtles
# Bandoni
# 1/31/20
# 
# This code animates pusheen going down stairs
#==========================

from turtle import * 
cat = Turtle()

from turtle import * 
dog = Turtle()

from turtle import * 
fish = Turtle()

money = Screen()
money.screensize(400,600)
money.update()

money.bgcolor('white') 
money.bgpic("codebackground1.gif") 
money.update() 

turtleimage = 'pusheen2.gif'
money.register_shape(turtleimage)
cat.shape(turtleimage)


cat.left(180)
cat.penup()
cat.forward(250)
cat.right(90)
cat.forward(200)
cat.backward(20)
## cat destination

dog.pensize(10)
dog.pencolor("#413EFA")
dog.penup()
dog.left(180)
dog.forward(300)
dog.right(90)
dog.forward(150)
dog.right(90)
dog.pendown()
##start of stairs
dog.forward(100)
dog.right(90)
dog.forward(65)
dog.left(90)

dog.forward(100)
dog.right(90)
dog.forward(65)
dog.left(90)

dog.forward(100)
dog.right(90)
dog.forward(65)
dog.left(90)

dog.forward(100)
dog.right(90)
dog.forward(65)
dog.left(90)

dog.forward(100)
dog.right(90)
dog.forward(65)
dog.left(90)
dog.forward(100)
##end of stairs

## start of dot
fish.penup()
fish.left(180)
fish.forward(250)
fish.right(90)
fish.forward(200)
fish.right(90)
fish.shape("circle")
fish.pencolor("red")
fish.fillcolor("red")
fish.forward(50)
fish.forward(50)
fish.right(90)
fish.forward(100)
fish.left(90)
##dot on stairs

fish.speed(15)
for x in range(90):
    fish.forward(1)
    fish.right(1)
fish.left(90)
fish.forward(80)
##repeate curve
cat.speed(15)
cat.right(90)
for x in range(90):
    cat.forward(1)
    cat.right(1)
cat.left(90)
cat.forward(80)
##cat

for x in range(90):
    fish.forward(1)
    fish.right(1)
fish.left(90)
fish.forward(80)
##fish
for x in range(90):
    cat.forward(1)
    cat.right(1)
cat.left(90)
cat.forward(80)
#cat

for x in range(90):
    fish.forward(1)
    fish.right(1)
fish.left(90)
fish.forward(80)
#fish

for x in range(90):
    cat.forward(1)
    cat.right(1)
cat.left(90)
cat.forward(80)


for x in range(90):
    fish.forward(1)
    fish.right(1)
fish.left(90)
fish.forward(80)

## start of cat going down

for x in range(90):
    cat.forward(1)
    cat.right(1)
cat.left(90)
cat.forward(80)


done()

