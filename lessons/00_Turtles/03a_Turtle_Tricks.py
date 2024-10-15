"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600, startx=0, starty=0)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina
def drawpolygon(sides): 
    angle=360/sides
    for i in range(sides):
        tina.forward(102)
        tina.left(angle)
   
drawpolygon(4)
tina.goto(0,102)
drawpolygon(3)

def drawhouse(x,y, color):
    tina.goto(x,y)
    drawpolygon(4)
    tina.goto(x,y+102)
    drawpolygon(3)
    tina.begin_fill()
    tina.color(color)
drawhouse(100,100, "red")
drawhouse(-100,-100, "blue")
turtle.exitonclick()                    # Close the window when we click on it
