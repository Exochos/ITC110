# smiles.py
# Assignment 4 for ITC110
# by: Jeremy Ward random.choice(colors)

from graphics import *
import random

def faces(x,y,m,win):

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
    random.seed()
    win = GraphWin("Faces", 500, 500)
    win.setBackground("Light Grey")

    for i in range(100):
        faces(random.randint(1,400)+20,random.randint(1,400)+20,random.randint(10,30),win)
        time.sleep(.200)
    win.getMouse()

main()
