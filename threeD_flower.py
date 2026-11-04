import turtle
import math
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Love Heart Animation")
screen.setup(width=800, height=700)

# Turtle setup
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# Heart coordinates
def heart(t):
    x = 16 * math.sin(t) ** 3
    y = (13 * math.cos(t)
         - 5 * math.cos(2 * t)
         - 2 * math.cos(3 * t)
         - math.cos(4 * t))
    return x, y

# Draw heart using "I love you"
def draw_heart(scale):
    t.clear()

    for i in range(0, 360, 3):
        angle = math.radians(i)

        x, y = heart(angle)

        # Position
        t.goto(x * scale, y * scale)

        # Text settings
        t.color("#ea80b0")
        t.write(
            "I miss you",
            align="center",
            font=("Arial", 10, "bold")
        )

    screen.update()


# Animation
screen.tracer(0)

for scale in range(14, 21):
    draw_heart(scale)
    time.sleep(0.08)

for scale in range(20, 14, -1):
    draw_heart(scale)
    time.sleep(0.08)

# Keep the heart on screen
draw_heart(18)

turtle.done()
