# smiles.py
# Assignment 4 for ITC110
# by: Jeremy Ward


# Various import statements
from graphics import *
import random


# Function Faces
# We are taking an x cord, a y cord, m is a size variable and win is passing the window object 
def faces(x,y,m,win):

    #Creating a circle to make the face
    #Using random int to color said face using rgb
    #using the for loop to make 2 eyes a bit appart
    #then using a line for the mouth
    face = Circle(Point(x,y), (m * 3))
    face.setFill(color_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    face.setOutline('black')
    face.draw(win)

    for i in range (0,2):
        eye = Circle(Point((x-m)+(30*i),(y-(m*1.5))), (m/3))
        eye.setFill('black')
        eye.setOutline('black')
        eye.draw(win)
    mouth = Line(Point((x+m),(y+m)),Point(x-m,y+m))
    mouth.draw(win)

def main():

    # Create a main window and setBackground color
    # also seeing the random function
    random.seed()
    win = GraphWin("Faces", 500, 500)
    win.setBackground("Light Grey")

    for i in range(100):
        # here we are calling the function with rando sizes roughly 100 times
        faces(random.randint(1,400)+20,random.randint(1,400)+20,random.randint(10,30),win)
        # sleep is here to make things look cooler
        time.sleep(.200)
    win.getMouse()

main()
