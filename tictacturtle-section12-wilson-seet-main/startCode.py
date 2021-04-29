"""
Created on Mon Oct  5 13:25:06 2020

@author: Dr. Z
@author: YOURNAME HERE

1. Read the code THOROUGHLY (there's something new for everyone)
2. Run the code
3. Change where required FIRST then continue editing.

DESCRIBE YOUR CHANGES HERE
"""
import turtle, random, time
turtle.tracer(0)

w=600
h=600
turtle.setup(w,h) # start with calling setup to turn on listeners
turtle.listen() # for keyboard listening

# =========DEFINE GLOBAL VARIABLES BELOW=========
panel=turtle.Screen()
running = True # for controlling the while loop


# this turtle is an example to demonstrate the functions below. You will likely
# have to DELETE OR MODIFY THIS TURTLE to get your game to work properly
testTudine = turtle.Turtle(shape='circle') # example turtle

# =========DEFINE FUNCTIONS BELOW=========


# ========= DEFINE LOCAL VARIABLES =========



# =========SET UP TURTLE(S) BELOW (color, size, shape, etc)=========


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