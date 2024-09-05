
""""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(100)                           # Make the turtle move as fast, but not too fast. 

def draw_polygon(sides):

    angle = 360/sides                    # Calculate angle from number of sides
    
    for i in range(sides):                 # Loop through the number of sides
        tina.forward(100)                              # Move tina forward by the forward distance
        tina.left(angle)                              # Turn tina left by the left turn


draw_polygon(4)                        # Draw a square

...                                      # Move tina to another spot on the screen

draw_polygon(5)                        # Draw a pentagon

...                                      # Move tina to another spot on the screen

draw_polygon(6)                        # Draw a hexagon

draw_polygon(7)
draw_polygon(8)
draw_polygon(9)
draw_polygon(10)
draw_polygon(11)
draw_polygon(12)
draw_polygon(13)
draw_polygon(14)
draw_polygon(15)

turtle.exitonclick()                     # Close the window when we click on it
