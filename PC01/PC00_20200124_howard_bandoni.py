#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PC## - Graffiti
# Howard, Bandoni
# 1/24/20
# 
# This code draws Graffiti Spelling HI
#==========================
# -*- coding: utf-8 -*-

from turtle import * #fetches turtle commands

money = Screen() #create one canvas for all of your turtles.


money.screensize(400,600)
money.update()

money.bgcolor('white') #set the canvas color to white
money.bgpic("gradient1.gif") #background image color is pink and purple
money.update() #updates to draw any changes made to the canvas

#Start of drawing
cat = Turtle()
cat.pensize(15)
cat.pencolor("white")
cat.showturtle()
cat.up()
cat.left(180)
cat.down()
cat.up()
cat.forward(180)
cat.down()
cat.hideturtle()
cat.right(90)
cat.forward(180)
cat.showturtle()
cat.down()
cat.backward(90)
cat.right(90)
cat.forward(60)
cat.down()
cat.right(90)
cat.forward(90)
cat.right(180)
cat.forward(180)
cat.right(90)
cat.penup()
cat.forward(90)
cat.right(90)
cat.pendown()
cat.forward(180)
##hi number one white

cat.right(90)
cat.penup()
cat.forward(170)
cat.right(90)
cat.forward(10)
cat.pencolor("pink") #chnages pen color to pink 
cat.pendown()
cat.forward(180)
cat.left(180)
cat.forward(90)
cat.left(90)
cat.forward(90)
cat.undo()
cat.left(90)
cat.forward(10)
cat.left(90)
cat.left(180)
cat.forward(60)
cat.right(90)
cat.right(180)
cat.forward(60)
cat.forward(20)
cat.right(180)
cat.forward(180)
cat.penup()
cat.left(90)
cat.forward(90)
cat.right(90)
cat.left(180)
cat.pendown()
cat.forward(180)
cat.hideturtle()
#end of hi number two

done()


