# file: mazesfinal.py

# Final Project for Comp Sci 1XA3

# a program that makes use of several algorithms to generate a maze with a START POINT, END POINT, and PICKS UP A KEY along the way

# START point is at the top left - point (1,1)
# END POINT is randomly generated
# KEY is randomly generated

# required imports
from random import *
from graphics import *


# opens window
win = GraphWin("ALYSSIA'S PERFECT MAZE", 750, 750)


## ------------------------------- x INITIAL PRINT STATEMENT x -------------------------------- ##

print()
print("--------------------------------")
print("Welcome to the Perfect Maze")
print("the final project for 1XA3!")
print("--------------------------------")
print()
print("The green dot is the STARTING POINT")
print("The yellow square is the KEY")
print("The red square is the FINISH POINT")
print("The blue squares are the PATH")
print()
print("--------------------------------")
print()
print("Wait for the program to generate the entire perfect maze first\nbased on the generated points")
print("then it will show you the correct path to the finish point.")
print()
print("The path values/co-ordinates to get to the end are printed at the \nend of the trace.")
print()
print("The program takes longer for larger mazes than shorter ones i.e Maze(10) \nvs Maze(15). For larger mazes, please be patient! Feel free to sip a drink\nor grab a snack :P")
print()
print("Type 'Maze(N)', N indicating the N*N size of the maze")

## ------------------------------- x MAZE CLASS x -------------------------------- ##

class Maze:

    # creates an N by N maze, constructor takes parameter N
    def __init__(self, N):
        
        self.visitedPoints = []     # visited poiints
        self.path = []
        self.x = True
        self.n = N

        # Must become True when the endpoint is reached in the maze
        self.exitFound = False      # stays false

        # The current row and current column are represented by currow and curcol
        self.curcol = 1             # value changes
        self.currow = 1             # value changes     

        # movex and movey represent the horizontal and vertical movements from the starting point.
        self.movex = 0              
        self.movey = 0

        # endrow and endcol represent the position of the door. 
        self.endrow = 0
        self.endcol = 0

        # The distance between lines are specified by numLines. 
        self.numLines = 500/self.n

        # The maze background is displayed
        pt = Point(0,0)
        pt.draw(win)
        rect2 = Rectangle(Point(500, 500), pt)
        rect2.setFill("black")
        rect2.draw(win)


        
## ------------------------------- x STARTING POINT x -------------------------------- ##


        # starting position dot 
        pt = Point((self.movex + 1)*self.numLines/2, (self.numLines - (self.movey*self.numLines))/2)
        cir = Circle(pt, 12)
        cir.setFill("green")
        cir.draw(win)

## ------------------------------- x WALLS x -------------------------------- ##


        # vertical walls
        for i in range(self.n + 1):
            pt = Point(0, i*self.numLines)
            pt.draw(win)
            line = Line(pt, Point(500, i*self.numLines))
            line.setFill("white")
            line.draw(win)
            
        # horizontal walls 
        for k in range(self.n + 1):
            pt = Point(k*self.numLines, 0)
            pt.draw(win)
            line = Line(pt, Point(k*self.numLines, 500))
            line.setFill("white")
            line.draw(win)


        # exit point is randomly selected using randrange
        while (True):
            self.endrow = randrange(((-1)*self.n) + 2, 1, 1)
            self.endcol = randrange(1, self.n, 1)
            if not (self.endrow == 1 and self.endcol == 1):
                break

        self.movex = self.endcol - 1
        self.movey = self.endrow - 1
        
        pt = Point(self.movex*self.numLines+15,(0 - (self.movey*self.numLines)) + 15)
        pt.draw(win)
        rect = Rectangle(Point((self.movex + 1)*self.numLines - 15, (self.numLines - (self.movey*self.numLines)) - 15), pt)
        rect.setFill("red")        
        rect.draw(win)
        
        self.movex = 0
        self.movey = 0      

        # call explore function
        # perfect maze generation
        
        self.explore()

## ------------------------------- x PUSH & POP FUNCTIONS / STACK x -------------------------------- ##

    # Basic stack operations such as pop and push are defined by the functions below:
        
    def push(self, item):
        if self.exitFound == False:
            self.path.append(item)
        else:
            return
 
    def pop(self):
        if self.exitFound == False:
            self.path.pop()
        else:
            return

    def stackSize(self):
        return len(self.path)
    
## ------------------------------------ x VISITED POINTS x ----------------------------------------- ##


    # list of visited points 
    def add(self, item):
        self.visitedPoints.append(item)
       
    def listSize(self):
        return len(self.visitedPoints)    

    # explore function generates perfect maze
    def explore(self):        
        
        totalCells = self.n*self.n
        visitedCells = 1

## ------------------------------- x STARTING POINT x -------------------------------- ##


        # start point pushed onto visited stack
        initialPoint = [1,1] # initial (1,1) point
        self.add(initialPoint)
        
        """ North = 1
            South = 2
            West = 3
            East = 4"""

## ------------------------------- x TRACKING MOVES x -------------------------------- ##


        # counter2 contains backtracked moves
        counter2 = 0

        # counter contains impossible moves
        counter = 0
     
        while visitedCells < totalCells: # makes all cells accessible 

            counter = 0       # must constantly set to zero

            num = randint(1, 4) # chooses direction at random

            # Moving beyond the maze's edges are impossible moves.
            if self.movex == 0:
                counter = counter + 1

            if self.movex == self.n - 1:
                counter = counter + 1

            if self.movey == 0:
                counter = counter + 1

            if self.movey == (-1*self.n) + 1:
                counter = counter + 1

## ------------------------------- x NO POSSIBLE MOVES x -------------------------------- ##


            # Checks if there are no possible moves from the current position
            for i in range(len(self.visitedPoints)):
                    
                    if self.visitedPoints[i] == [self.curcol, self.currow + 1] or self.visitedPoints[i]== [self.curcol, self.currow - 1] or self.visitedPoints[i]== [self.curcol - 1, self.currow] or self.visitedPoints[i]== [self.curcol + 1, self.currow]:

                        counter = counter + 1
                        
                    if counter >= 4:
                        
                        if self.stackSize() >= 1:
                            self.pop()
                            
                        counter2 = counter2 + 1
                        previous = self.visitedPoints[len(self.visitedPoints) - counter2]
                        self.curcol = previous[0]
                        self.currow = previous[1]
                        self.movex = previous[0] - 1
                        self.movey = previous[1] - 1                            
                        counter = 0
            counter = 0

## ------------------------------- x DIRECTIONS x --------------------------------------- ##

                            
            # if a North move is within the maze, continue             
            if (num == 1) and (self.movey < 0):

                self.x = True

                # checks if the point checked has already been visited
                for i in range(0, self.listSize()):
                    if self.visitedPoints[i] == [self.curcol, self.currow + 1]:
                        self.x = False
                        break
                        
                # If space is free, wall is broken down   
                if self.x == True:
                    
                    self.currow = self.currow + 1
                    newPoint = [self.curcol, self.currow]
                    self.add(newPoint)
                    self.push(newPoint)

                    # Exit found, exitFound is now TRUE
                    if newPoint == [self.endcol, self.endrow]:
                        self.exitFound = True
                        
                    self.movey = self.movey + 1
                    visitedCells = visitedCells + 1

                    pt = Point(self.movex*self.numLines, self.numLines - (self.movey*self.numLines))
                    pt.draw(win)
                    rect = Rectangle(Point((self.movex + 1)*self.numLines, self.numLines - (self.movey*self.numLines)), pt)
                    rect.setFill("black")        
                    rect.draw(win)

                    counter2 = 0
                    
            # same is done for South (2), West (3), and East(4)
                
            elif num == 2 and (self.movey > (- 1*self.n) + 1): # south

                self.x = True

                for i in range(0, self.listSize()):
                    if self.visitedPoints[i] == [self.curcol, self.currow - 1]:
                        self.x = False
                        break                        
                    
                if self.x == True:
                    
                    self.currow = self.currow - 1                    
                    newPoint = [self.curcol, self.currow]
                    self.add(newPoint)
                    self.push(newPoint)

                    # Exit found, exitFound becomes TRUE
                    if newPoint == [self.endcol, self.endrow]:
                        self.exitFound = True

                    self.movey = self.movey - 1
                    visitedCells = visitedCells + 1

                    pt = Point(self.movex*self.numLines, 0 -( self.movey*self.numLines))
                    pt.draw(win)
                    rect = Rectangle(Point((self.movex + 1)*self.numLines, 0 - (self.movey*self.numLines)), pt)
                    rect.setFill("black")        
                    rect.draw(win)
                    
                    counter2 = 0                    
                
            elif num == 3 and (self.movex > 0): # west

                self.x = True

                for i in range(0, self.listSize()):
                    if self.visitedPoints[i] == [self.curcol - 1, self.currow]:
                        self.x = False
                        break                        
                    
                if self.x == True:
                    
                    self.curcol = self.curcol - 1
                    newPoint = [self.curcol, self.currow]
                    self.add(newPoint)
                    self.push(newPoint)


                    # Exit found, exitFound becomes TRUE 
                    if newPoint == [self.endcol, self.endrow]:
                        self.exitFound = True

                    self.movex = self.movex - 1
                    visitedCells = visitedCells + 1

                    pt = Point((self.movex + 1)*self.numLines, 0 - (self.movey*self.numLines))
                    pt.draw(win)
                    rect = Rectangle(Point((self.movex+1)*self.numLines, self.numLines-(self.movey*self.numLines)), pt)
                    rect.setFill("black")        
                    rect.draw(win)

                    counter2 = 0
                
            elif num == 4 and (self.movex < self.n - 1): # east

                self.x = True

                for i in range(0,self.listSize()):
                    if self.visitedPoints[i] == [self.curcol + 1, self.currow]:
                        self.x = False
                        break                        
                    
                if self.x == True:
                    
                    self.curcol = self.curcol + 1
                    newPoint = [self.curcol, self.currow]
                    self.add(newPoint)
                    self.push(newPoint)

                    # Exit found, exitFound = True
                    if newPoint == [self.endcol, self.endrow]:
                        self.exitFound = True

                    self.movex = self.movex + 1
                    visitedCells = visitedCells + 1

                    pt = Point(self.movex*self.numLines,0 - (self.movey*self.numLines))
                    pt.draw(win)
                    rect = Rectangle(Point(self.movex*self.numLines, self.numLines - (self.movey*self.numLines)), pt)
                    rect.setFill("black")        
                    rect.draw(win)

                    counter2 = 0
            
            
            self.x = True


## ------------------------------- x COLOURED PATH x -------------------------------- ##
            
        print()
        print("-------------------")
        print("This is the path:")
        print("-------------------")
        print()
        
        for i in range(0, self.stackSize() - 1):
            print(self.path[i])  # prints path points to get to the finish point
                                 # there is ALWAYS a defined singular path to the exit, however, sometimes blue path squares are not printed on all of the
                                 # cells and sometimes skips squares or sections
                                 # but do know that there are NO circles in the maze and there is always a clear path from start to finish with a key
                                 # along the way

            current = self.path[i]

            self.movex = current[0] - 1
            self.movey = current[1] - 1

            pt = Point(self.movex*self.numLines + 15,(0 -(self.movey*self.numLines)) + 15)
            pt.draw(win)
            rect = Rectangle(Point((self.movex + 1)*self.numLines - 15, (self.numLines - (self.movey*self.numLines)) - 15), pt)
            rect.setFill("blue")        
            rect.draw(win)

## ------------------------------- x KEY GENERATION x -------------------------------- ##


        randomLocation = randrange(1, self.stackSize() - 1)   # chooses random location based on points on the stack

        current = self.path[randomLocation]

        self.movex = current[0] - 1
        self.movey = current[1] - 1

        # key graphics

        pt = Point(self.movex*self.numLines+15,(0 - (self.movey*self.numLines)) + 15)
        pt.draw(win)
        rect = Rectangle(Point((self.movex+1)*self.numLines - 15, (self.numLines - (self.movey*self.numLines)) - 15), pt)
        rect.setFill("yellow")          
        rect.draw(win)
