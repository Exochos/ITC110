# graphicOne.py
# Assignment 4 for ITC110
# by: Jeremy Ward

from graphics import *

def main():

    # Create a main window and setBackground color
    win = GraphWin("Christmas Scene", 500, 500)
    win.setBackground("Light Blue")

    # Draws the First of many circles
    # This is going to be my snowman
    center = Point(125,425)
    circ = Circle(center,90)
    circ.setFill('white')
    circ.setOutline('white')
    circ.draw(win)

    # More cirlces
    center = Point(125,300)
    circ2 = Circle(center,70)
    circ2.setFill('white')
    circ2.setOutline('white')
    circ2.draw(win)

    # More cirlces
    center = Point(125,200)
    circ3 = Circle(center,50)
    circ3.setFill('white')
    circ3.setOutline('white')
    circ3.draw(win)

    # we are drawing the belly dots here
    for i in range(3):
        dot = Point(125, (275 + i * 20))
        dot = Circle(dot, 5)
        dot.setFill('black')
        dot.draw(win)

    # still more circles
    center = Point(110,190)
    circ9 = Circle(center,5)
    circ9.setFill('black')
    circ9.setOutline('black')
    circ9.draw(win)

    # still more cirlces
    center = Point(140,190)
    circ9 = Circle(center,5)
    circ9.setFill('black')
    circ9.setOutline('black')
    circ9.draw(win)

    # Here we are drawing the hat
    hatOne = Rectangle(Point(90,150), Point(160,160))
    hatOne.setFill('black')
    hatOne.draw(win)
    hatOne = Rectangle(Point(100,120), Point(150,160))
    hatOne.setFill('black')
    hatOne.draw(win)

    # Here we are making a carrot
    carrot = Polygon(Point(120,190), Point(115,210), Point(135,200))
    carrot.setFill('orange')
    carrot.setOutline('orange')
    carrot.draw(win)

    #loop to make a mouth with a series of circles
    for i in range(5):
        m = Point((100 + i * 10),220)
        mouth = Circle(m,2)
        mouth.setFill('black')
        mouth.draw(win)

    # drawing the bottom of the tree
    for i in range(1,6):
        tree = Rectangle(Point(330+(i*5),400), Point(400-(i*5),500))
        tree.setFill('chocolate')
        tree.setOutline('black')
        tree.draw(win)

#
#   we are doing a bunch of stuff here
#   including drawing the tree itself and
#   then drawing thre different types of balls to make it look festive
#

    for i in range(0,8):
        n = i * 10
        treeGreen = Polygon(Point((260 + n),(400 - (n*3))),Point((470 - n),((400-n*3))),Point((375),(250 - (n*3))))
        treeGreen.setFill('green')
        treeGreen.setOutline('black')
        treeGreen.draw(win)

        center = Point(260 + n, 400 - (n*3))
        ball = Circle(center,5)
        ball.setFill('gold')
        ball.setOutline('black')
        ball.draw(win)

        center2 = Point(470 - n, 400 - (n*3))
        ball2 = Circle(center2,5)
        ball2.setFill('gold')
        ball2.setOutline('black')
        ball2.draw(win)

    for i in range(10):
            center3 = Point((373 - i),(40 + (i * 39)))
            ball3 = Circle(center3,5)
            ball3.setFill('silver')
            ball3.draw(win)

    # ths is here cause otherwise the tree will disappear to quickly
    win.getMouse()

main()
