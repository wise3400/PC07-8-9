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
buffer=20
running=True
shape =True

numturts=9
turts=[]
cordinates =[(-180,180),(-180,0),(-180,-180),(0,180),(0,0),(0,-180),(180,180),(180,0),(180,-180)]

for i in range(numturts): #adds all the turtles to the list
  turts.append(turtle.Turtle())

# =========DEFINE FUNCTIONS BELOW=========
def image(x,y): #click function
  global shape  
  for i in range(len(turts)):
    turtX = turts[i].xcor()
    turtY = turts[i].ycor()
    if round(turtX)-20 <= round(x) <= round(turtX)+20 and round(turtY)-20 <= round(y) <= round(turtY)+20:
      selected = i
      if (shape == True):
        turts[i].shape('biden.gif')
      else:
        turts[i].shape('trump.gif')
      print(shape)
      print(selected)
      shape = not shape
      break
      
# ========= DEFINE LOCAL VARIABLES =========

# =========SET UP TURTLE(S) BELOW (color, size, shape, etc)=========
for i in range(numturts):#sets up the "square"
  turts[i].shape("square")
  turts[i].turtlesize(8)
  turts[i].up()
  turts[i].goto(cordinates[i])

# CALLBACK FUNCTIONS BELOW   
for i in range(len(turts)):#applies the function to all the turtles
    turts[i].onclick(image)

# =========ANIMATIONS BELOW=========
# code will execute in order within the loop
while running:
    
    # YOUR ANIMATION CODE HERE
    
    panel.update()


# =========LISTENERS & CLEANUP =========
panel.mainloop() # keep listeners listening DO NOT DELETE
turtle.done() # cleanup whenever we exit the loop DO NOT DELETE.