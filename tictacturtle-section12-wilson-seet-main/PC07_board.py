"""
Created on October 16th, 2020
@author: Wilson Seet & Noah Hubbard
Description & Rules:
Over here, we just created the tic tac toe board.

"""
from turtle import *
import turtle, random
turtle.bgcolor("lightblue")
turtle.colormode(255)
turtle.tracer(0) 
w=600
h=600
turtle.setup(w,h) # start with calling setup to turn on listeners
turtle.listen() # for keyboard listening

# =========DEFINE GLOBAL VARIABLES BELOW=========
panel=turtle.Screen()
running = True # for controlling the while loop
makeboard = turtle.Turtle()
# =========DEFINE FUNCTIONS BELOW=========
def board():
  makeboard.pensize(20)
  makeboard.color("darkblue")
#Horizontal Rows
  xRow = -250
  yRow = -100
  rowForward = 500
  for row in range(2):
    makeboard.penup()
    makeboard.goto(xRow, yRow)
    makeboard.pendown()
    makeboard.forward(rowForward)
    yRow = 100

#Vertical Columns
  makeboard.left(90)
  xColumn = 100
  yColumn = -250
  columnForward = 500
  for column in range(2):
    makeboard.penup()
    makeboard.goto(xColumn, yColumn)
    makeboard.pendown()
    makeboard.forward(columnForward)
    xColumn = -xColumn
board() 
# ========= DEFINE LOCAL VARIABLES =========



# =========SET UP TURTLE(S) BELOW (color, size, shape, etc)========




# CALLBACK FUNCTIONS BELOW 
# add onclick and onkey commands below. 


# notice that onclick is attached to the TURTLE, not the panel.

# =========ANIMATIONS BELOW=========
# code will execute in order within the loop
while running:
    
    # YOUR ANIMATION CODE HERE
    
    
    
    
    panel.update()


# =========LISTENERS & CLEANUP =========
panel.mainloop() # keep listeners listening DO NOT DELETE
turtle.done() # cleanup whenever we exit the loop DO NOT DELETE.
