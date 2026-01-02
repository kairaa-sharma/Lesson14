import turtle  

colors = ["red", "purple", "blue", "green", "orange", "yellow"]

# Create the turtle object
my_pen = turtle.Turtle() 
turtle.bgcolor("black")
my_pen.speed(0) # Set to fastest speed so you don't have to wait

for x in range(360):
    # Use .pencolor() instead of .colors()
    my_pen.pencolor(colors[x % 6]) 
    my_pen.width(x/100 + 1)
    my_pen.forward(x)
    my_pen.left(59)

turtle.done()