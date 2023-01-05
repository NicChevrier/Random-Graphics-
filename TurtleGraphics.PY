import turtle
import random

# Set the turtle's speed to the maximum
turtle.speed('fastest')

# Set the turtle's pen size to a random value between 1 and 10
turtle.pensize(random.randint(1, 10))

# Set the turtle's pen color to a random color
turtle.pencolor(random.random(), random.random(), random.random())

# Move the turtle to a random location on the screen
turtle.penup()
turtle.setx(random.randint(-200, 200))
turtle.sety(random.randint(-200, 200))
turtle.pendown()

# Draw a random polygon with a random number of sides
num_sides = random.randint(3, 12)
for _ in range(num_sides):
    turtle.forward(50)
    turtle.right(360 / num_sides)

# Hide the turtle
turtle.hideturtle()

# Keep the window open until it is closed
turtle.exitonclick()
