# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 13:25:06 2020
@author: Noah Hubbard
@author: Wilson Seet
1. Read the code THOROUGHLY (there's something new for everyone)
2. Run the code
3. Change where required FIRST then continue editing.
"""
import turtle, random, time, numpy as np, checkwin
turtle.tracer(0)
turtle.bgcolor("lightblue")
turtle.colormode(255)

w=600
h=600
turtle.setup(w,h) # start with calling setup to turn on listeners
turtle.listen() # for keyboard listening

# =========DEFINE GLOBAL VARIABLES BELOW=========
panel=turtle.Screen()
panel.register_shape('biden.gif')
panel.register_shape('trump.gif')
startgame= False

#========== NEW CLASS ========
#Modified Dr. Z's code...
class createGameManager:
  def __init__(self):
    self.trump_biden_IMG = "biden_trump.gif"
    self.makesplashTurt = turtle.Turtle()
    self.text = turtle.Turtle(visible=False)
    self.font = ('Times', 14,'bold')
    self.board=board()
    self.p1=player()
    self.p1.makeBoardList()
    panel.onkeypress(self.clearScreen,"Return")
    self.drawSplash()
  def clearScreen(self):
    # clears screen on keypress
    self.makesplashTurt.clear()
    self.makesplashTurt.hideturtle()
    self.text.clear()
    self.board.drawboard()
    self.p1.setUp()
    panel.update()
  def drawSplash(self):
    # set turtle to be an image
    panel.addshape(self.trump_biden_IMG)
    self.makesplashTurt.shape(self.trump_biden_IMG)
    # draw image in center (home)
    self.makesplashTurt.stamp()
    # add text, color, and positions
    self.text.up()
    self.text.goto(27,-160)
    self.text.color("purple")
    self.text.write("Press ENTER/RETURN to begin BATTLE!", align='Center',font=self.font)
    #2020 , biden
    self.text.goto(-220,0)
    self.text.color("darkblue")
    self.text.write("2020", align = 'center', font=self.font)
    #2020, trump
    self.text.goto(211,0)
    self.text.color("red")
    self.text.write("2020", align = 'center', font=self.font)


#========== NEW CLASS=========
class board: 
  def __init__(self):
    self.makeboard = turtle.Turtle()
    self.xRow = -250
    self.yRow = -100
    self.vertx = 100
    self.verty = -250
    self.rowForward = 500
  def drawboard(self):
    self.makeboard.pensize(20)
    #Horizontal Columns
    for row in range(2):
      self.makeboard.color("blue")
      self.makeboard.penup()
      self.makeboard.goto(self.xRow, self.yRow)
      self.makeboard.pendown()
      self.makeboard.forward(self.rowForward)
      self.yRow = 100
    #Vertical Columns
    self.makeboard.left(90)
    self.columnForward = 500
    for column in range(3):
      self.makeboard.color("red")
      self.makeboard.penup()
      self.makeboard.goto(self.vertx, self.verty)
      self.makeboard.pendown()
      self.makeboard.forward(self.columnForward)
      self.vertx = -self.vertx

#=========NEW CLASS===========
class player:
    def __init__(self):
        self.buffer=20
        self.shape =True
        self.numturts=9
        self.turts=[]
        self.cordinates =[(-180,180),(-180,0),(-180,-180),(0,180),(0,0),(0,-180),(180,180),(180,0),(180,-180)]
        self.empty=''
        self.boardList=self.makeBoardList(empty = self.empty)
        self.size=3
    def makeBoardList(self,numside=3,empty=[]):
        '''Makes an empty scoreboard for tictactoe, based on the number of sides.
        The default 3x3 looks like this:
            [ [ [],[],[] ],
              [ [],[],[] ],
              [ [],[],[] ] ]
        Parameters-
        numside - (int) number of squares per side of the tic tac toe board
        empty - the indicator to use for an empty board. Try 0 or a string value.'''
        boardList=[]
        for i in range(numside):
            #make rows
            boardRow=[]
            for k in range(numside):
                # make columns
                boardRow.append(empty)
            boardList.append(boardRow)
        return(boardList)
        print(boardList)
        # return boardList
    def maketurts(self):
        for i in range(self.numturts):
            self.turts.append(turtle.Turtle())
            self.turts[i].shape("square")
            self.turts[i].turtlesize(6)
            self.turts[i].color("lightblue")
            self.turts[i].up()
            self.turts[i].goto(self.cordinates[i])
            panel.update()
    def image(self,x,y):
        # clicked = self.image(x,y)
        for i in range(len(self.turts)):
          turtX = self.turts[i].xcor()
          turtY = self.turts[i].ycor()
          if round(turtX)-20 <= round(x) <= round(turtX)+20 and round(turtY)-20 <= round(y) <= round(turtY)+20:
            if (self.shape == True):
              self.turts[i].shape('biden.gif')
              self.boardList[int(i/self.size)][i%self.size]='O'
              print(self.boardList[0],'\n',
              self.boardList[1],'\n',
              self.boardList[2])
            else:
              self.turts[i].shape('trump.gif')
              self.boardList[int(i/self.size)][i%self.size]='X'
              print(self.boardList[0],'\n',
              self.boardList[1],'\n',
              self.boardList[2])
            self.shape = not self.shape
        self.CheckForWin()
        # i=clicked
        # return(clicked)
        panel.update()
    def CheckForWin (self):
        WINNER = checkwin.checkWin(self.boardList)
        print(WINNER)
        
        if type(WINNER) == str and WINNER != self.empty:
            gameOver = True
        else:
            for row in self.boardList:
                if self.empty in row:
                    print(self.boardList)
                    gameOver = False
                    break
                else:
                    gameOver = True
                    print("It's a draw! No Winner!")
                    break
        if gameOver:
            print('Game Over')
            if WINNER=='O':
                print("Biden has won the presidency!")
            elif WINNER =='X':
                print("Well, I guess Trump won")
    def setUp(self):
      self.maketurts()
      # self.posturts()
      for i in range(len(self.turts)):#applies the function to all the turtles
        self.turts[i].onclick(self.image)
            
#========create objects ===========
game = createGameManager()       


# =========LISTENERS & CLEANUP =========
panel.mainloop() # keep listeners listening DO NOT DELETE
turtle.done() # cleanup whenever we exit the loop DO NOT DELETE.