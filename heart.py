import turtle
import random
import math
# ---------------- SCREEN SETUP ----------------
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Glowing Heart")
screen.setup(width=900, height=700)
# ---------------- MAIN TURTLE ----------------
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
# ---------------- HEART FUNCTION ----------------
def draw_heart(size, color, width):
    t.penup()
    t.goto(0, -size * 0.5)
    t.setheading(140)
    t.pendown()
    t.color(color)
    t.pensize(width)
    t.begin_fill()
    # Left side
    t.forward(size)
    # Left curve
    for i in range(200):
        t.right(1)
        t.forward(size / 100)
    # Top center
    t.left(120)
    # Right curve
    for i in range(200):
        t.right(1)
        t.forward(size / 100)
    # Right side
    t.forward(size)
    t.end_fill()
# ---------------- GLOW EFFECT ----------------
# Draw larger hearts first
draw_heart(220, "darkred", 2)
draw_heart(210, "red", 2)
draw_heart(200, "red", 3)
draw_heart(190, "deeppink", 3)
draw_heart(180, "hotpink", 3)
# Bright inner heart
draw_heart(165, "red", 4)
# ---------------- SPARKLES ----------------
sparkle = turtle.Turtle()
sparkle.speed(0)
sparkle.hideturtle()
sparkle.color("white")
def draw_sparkle(x, y, size):
    sparkle.penup()
    sparkle.goto(x, y)
    sparkle.setheading(45)
    sparkle.pendown()
    sparkle.pensize(2)
    # Vertical line
    sparkle.forward(size)
    sparkle.backward(size * 2)
    sparkle.forward(size)
    # Horizontal line
    sparkle.right(90)
    sparkle.forward(size)
    sparkle.backward(size * 2)
    sparkle.forward(size)
# Random stars
random.seed(10)
for i in range(80):
    x = random.randint(-420, 420)
    y = random.randint(-300, 300)
    # Keep stars away from the center heart
    if -230 < x < 230 and -180 < y < 180:
        continue
    size = random.randint(2, 8)
    draw_sparkle(x, y, size)
# ---------------- BIG SPARKLE ----------------
big = turtle.Turtle()
big.speed(0)
big.hideturtle()
big.color("white")
big.pensize(3)
big.penup()
big.goto(0, 120)
big.setheading(90)
big.pendown()
big.forward(30)
big.backward(60)
big.forward(30)
big.right(90)
big.forward(30)
big.backward(60)
# ---------------- HEART REFLECTION ----------------
reflection = turtle.Turtle()
reflection.speed(0)
reflection.hideturtle()
for i in range(12):
    reflection.penup()
    reflection.goto(-70 + i * 5, -130 - i * 8)
    reflection.setheading(0)
    reflection.pendown()
    reflection.color("darkred")
    reflection.pensize(2)
    reflection.forward(140 - i * 10)
# ---------------- WATER WAVES ----------------
wave = turtle.Turtle()
wave.speed(0)
wave.hideturtle()
wave.color("darkred")
wave.pensize(1)
for i in range(12):
    y = -230 - i * 10
    wave.penup()
    wave.goto(-180 + i * 5, y)
    wave.setheading(0)
    wave.pendown()
    wave.forward(360 - i * 10)
# ---------------- TEXT ----------------
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(0, 280)
text.color("white")
text.write(
    "GLOWING HEART",
    align="center",
    font=("Arial", 28, "bold")
)
text.goto(0, -320)
text.color("pink")
text.write(
    "Made with Python Turtle",
    align="center",
    font=("Arial", 14, "normal")
)
# ---------------- FINISH ----------------
turtle.done()