import turtle # Importing Library
turtle.Screen().bgcolor("Light blue")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle() # Defined Variable

num_sides = 6 # Variable
side_length = 70
angle = 360.0 / num_sides
# Iterate loo[ for total number of side
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()