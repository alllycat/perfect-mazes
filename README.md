# Perfect-Mazes
###Intro to CS Class Final Project

A python program that makes use of several algorithms to generate a **perfect maze** of n times n. 

* **Perfect Maze**: one without any loops or closed circuits, and without any inaccessible areas. Also called a simply-connected Maze. From each point, there is exactly one path to any other point. The Maze has exactly one solution. In Computer Science terms, such a Maze can be described as a spanning tree over the set of cells or vertices.

* User calls **Maze(n)** function
* Program generates a maze with dimensions **n by n**
* Generates a **START** (green) / **END** POINT (red)
* A **KEY** (yellow) must be picked up before reaching the end point
* Generates a **path** (blue) from start to end points while picking up the key
* Prints out a **list of co-ordinates** for the **path** (blue)

![](http://i.imgur.com/0ocBxyT.png)

* **START POINT** is ALWAYS generated on the top left corner (1,1)
* **END POINT** is randomly generated
* **KEY POINT** is randomly generated 
* Perfect Maze is created based on START, END and KEY points
* **PATH POINTS** are then generated

####Maze(7) - (7*7 perfect maze)
![](http://i.imgur.com/tqdzBui.png)
####Maze(13) - (13*13 perfect maze)
![](http://i.imgur.com/J0AceiH.png)

### ** THINGS TO NOTE: ** 

* 1) The stack operations and maze objects are all defined under the Maze class, therefore there is no myStack class
* 2) There is ALWAYS a defined singular path to the exit, however, sometimes blue path squares are not generated on all of the cells leading up to the end point
* 3) There is always a clear path generated from start to finish with a key along the way (singular path can always be traced)

