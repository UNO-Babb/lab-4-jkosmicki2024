#TurtleGraphics.py
#Name: Jacob
#Date: 2/13/2025
#Assignment: Lab 4

hideturtle() 
def drawSquare(myturtle, size):
    for i in range(4):
        myturtle.forward(size)
        myturtle.right(90)

def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(150)
        bob.right(360/sides)
        
def squaresInSquares(myturtle, num):
    size = 150
    for i in range(num):
        myturtle.penup()
        myturtle.goto(-size / 2,size / 2)
        myturtle.pendown()
        drawSquare(myturtle, size)
        size-=10
        
def fillCorner(fetty, corner):
    drawSquare(fetty, 100)
    if corner == 1:
        fetty.begin_fill()
        drawSquare(fetty, 25)
        fetty.end_fill()
    if corner == 2:
        fetty.begin_fill()
        drawSquare(fetty, 25)
        fetty.end_fill()

def main():
    myturtle = turtle.Turtle()
    
    drawPolygon(myturtle, 5) #draws a pentagon
    # drawPolygon(myturtle, 8) #draws an octogon

    # fillCorner(myturtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myturtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myturtle, 5) #draws 5 concentric squares
    # squaresInSquares(myturtle, 3) #draws 3 concentric squares


main()
