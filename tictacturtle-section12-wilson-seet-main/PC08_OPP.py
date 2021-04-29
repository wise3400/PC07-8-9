# -*- coding: utf-8 -*-
""""
Created on Mon Oct  5 13:25:06 2020
@author: Noah Hubbard
@author: Wilson Seet
1. Read the code THOROUGHLY (there's something new for everyone)
2. Run the code
3. Change where required FIRST then continue editing.
"""
import turtle, random, time
turtle.tracer(0)

w=600
h=600
turtle.setup(w,h) # start with calling setup to turn on listeners
turtle.listen() # for keyboard listening

# =========DEFINE GLOBAL VARIABLES BELOW=========
panel=turtle.Screen()
panel.register_shape('biden.gif')
panel.register_shape('trump.gif')

class player:
  def __init__(self):
    self.buffer=20
    self.running=True
    self.shape =True
    self.numturts=9
    self.turts=[]
    self.cordinates =[(-180,180),(-180,0),(-180,-180),(0,180),(0,0),(0,-180),(180,180),(180,0),(180,-180)]
  def maketurts (self):
    for i in range(self.numturts): #adds all the turtles to the list
      self.turts.append(turtle.Turtle())

# =========DEFINE FUNCTIONS BELOW=========
  def image(self,x,y): #click function
    global shape
    for i in range(len(self.turts)):
      turtX = self.turts[i].xcor() # CHECK THESE LINES
      turtY = self.turts[i].ycor()
    if round(turtX)-20 <= round(x) <= round(turtX)+20 and round(turtY)-20 <= round(y) <= round(turtY)+20:
      selected = i
      if (self.shape == True):
        self.turts[i].shape('biden.gif')
      else:
        self.turts[i].shape('trump.gif')
      print(self.shape)
      print(self.selected)
      self.shape = not self.shape
# =========SET UP TURTLE(S) BELOW (color, size, shape, etc)=========
  def posturts(self):
    for i in range(self.numturts):#sets up the "square"
      self.turts[i].shape("square")
      self.turts[i].turtlesize(8)
      self.turts[i].up()
      self.turts[i].goto(self.cordinates[i])
# # CALLBACK FUNCTIONS BELOW
  def call(self):  
      for i in range(len(self.turts)):#applies the function to all the turtles
        self.turts[i].onclick(self.image) #CHECK THIS

p1 = player()
p2 = player()
# # =========ANIMATIONS BELOW=========
# # code will execute in order within the loop
# while running:
    
#     # YOUR ANIMATION CODE HERE
    
#     panel.update()


# =========LISTENERS & CLEANUP =========
panel.mainloop() # keep listeners listening DO NOT DELETE
turtle.done() # cleanup whenever we exit the loop DO NOT DELETE.