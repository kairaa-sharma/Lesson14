import turtle 

loadWindow = turtle.Screen()
turtle.Screen().bgcolor("Light blue")
turtle.speed(2)

for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.exitonclick()