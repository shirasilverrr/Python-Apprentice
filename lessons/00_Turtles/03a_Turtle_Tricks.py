"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600, startx=0, starty=0)    # Set the size of the window

tina = turtle.Turtle()  
tina.speed(10)                # Create a turtle named tina
def drawpolygon(sides): 
    angle=360/sides
    for i in range(sides):
        tina.forward(102)
        tina.left(angle)


def drawhouse(x,y, color):
    tina.penup()
    tina.goto(x,y)
    tina.pendown()
    tina.begin_fill()
    tina.color(color)
    drawpolygon(4)
    tina.goto(x,y+102)
    drawpolygon(3)
    tina.end_fill()


drawhouse(100,100, "red")
drawhouse(-100,-100, "blue")
drawhouse(50,50, "orange")
drawhouse(-50,-50, "pink")
drawhouse(-50,100, "purple")
drawhouse(100,50, "green")
drawhouse(-100,50, "brown")
drawhouse(-200,50, "yellow")
drawhouse(-150,150, "grey")
drawhouse(50,-100, "magenta")
drawhouse(0,-50, "navy blue")
drawhouse(0,-100, "pink")
drawhouse(0,-150, "purple")
drawhouse(50,100, "red")
drawhouse(50,200, "yellow")
drawhouse(50,0, "grey")
drawhouse(100,0, "blue")
drawhouse(100,150, "orange")
drawhouse(100,200, "brown")
drawhouse(150,0, "magenta")
drawhouse(150,50, "yellow")
drawhouse(-300,-100, "#39ad41")
drawhouse(-250,-200, "#f525c1")
tina.penup()
tina.goto(240,-240)
tina.write("shira silver")
turtle.exitonclick()                    # Close the window when we click on it
