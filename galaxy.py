import turtle
import colorsys
import random
import math

# ---------------- SCREEN SETUP ----------------
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("🌌 Colorful Galaxy - Turtle Graphics")
screen.setup(width=900, height=700)

# ---------------- MAIN TURTLE ----------------
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# ---------------- DRAW GALAXY SPIRAL ----------------
h = 0

for i in range(360):

    # Rainbow color
    r, g, b = colorsys.hsv_to_rgb(h, 1, 1)
    t.color(r, g, b)

    # Spiral movement
    t.forward(i * 1.5)
    t.right(91)

    # Draw small circles
    if i % 12 == 0:
        t.begin_fill()
        t.circle(5)
        t.end_fill()

    h += 0.003


# ---------------- STAR TURTLE ----------------
star = turtle.Turtle()
star.speed(0)
star.hideturtle()

# Generate random stars
random.seed(10)

for i in range(80):

    x = random.randint(-430, 430)
    y = random.randint(-320, 320)

    # Avoid too many stars near center
    if abs(x) < 150 and abs(y) < 100:
        continue

    star.penup()
    star.goto(x, y)
    star.pendown()

    size = random.randint(2, 5)
    star.color("white")

    star.begin_fill()
    star.circle(size)
    star.end_fill()


# ---------------- CENTER PLANET ----------------
planet = turtle.Turtle()
planet.speed(0)
planet.hideturtle()

planet.penup()
planet.goto(0, -55)
planet.pendown()

planet.color("cyan")
planet.begin_fill()
planet.circle(55)
planet.end_fill()

# Planet ring
planet.penup()
planet.goto(-85, 5)
planet.setheading(15)
planet.pendown()

planet.color("white")
planet.width(4)

planet.circle(90, 180)
planet.circle(90, 180)


# ---------------- SMALL PLANETS ----------------
planets = [
    (250, 150, 18, "orange"),
    (-280, 170, 14, "red"),
    (300, -180, 12, "yellow"),
    (-320, -180, 20, "violet")
]

for x, y, size, color in planets:

    planet.penup()
    planet.goto(x, y - size)
    planet.pendown()

    planet.color(color)
    planet.begin_fill()
    planet.circle(size)
    planet.end_fill()


# ---------------- DECORATIVE ORBITS ----------------
orbit = turtle.Turtle()
orbit.speed(0)
orbit.hideturtle()
orbit.width(1)

for radius in [100, 140, 180, 220]:

    orbit.penup()
    orbit.goto(0, -radius)
    orbit.setheading(0)
    orbit.pendown()

    orbit.color("gray")
    orbit.circle(radius)


# ---------------- TITLE ----------------
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(0, 300)

text.color("white")
text.write(
    "🌌 COLORFUL GALAXY 🌌",
    align="center",
    font=("Arial", 24, "bold")
)


# ---------------- FINAL MESSAGE ----------------
text.goto(0, -330)

text.color("cyan")
text.write(
    "Created using Python Turtle",
    align="center",
    font=("Arial", 14, "normal")
)

# ---------------- FINISH ----------------
turtle.done()