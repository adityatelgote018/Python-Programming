import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Turtle Mandala")

# Turtle setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# Starting hue
h = 0

# Draw colorful mandala
for i in range(72):

    # Change color
    color = colorsys.hsv_to_rgb(h, 1, 1)
    t.color(color)

    # Draw petals
    for j in range(6):
        t.circle(120)
        t.right(60)

    # Move to next position
    t.right(5)

    # Change color gradually
    h += 1 / 72

# Draw inner circle
t.penup()
t.goto(0, -50)
t.pendown()

t.color("white")
t.circle(50)

# Draw small decorative circles
for i in range(36):
    t.penup()
    t.goto(0, 0)
    t.setheading(i * 10)
    t.forward(170)
    t.pendown()

    t.color("yellow")
    t.begin_fill()
    t.circle(8)
    t.end_fill()

# Finish
turtle.done()