import turtle

t = turtle.Turtle()
t.speed(0)

turtle.bgcolor("black")

colors = ["red", "yellow", "blue", "green", "orange", "purple"]

for i in range(36):
    t.color(colors[i % 6])

    for j in range(4):
        t.forward(100)
        t.right(90)

    t.right(10)

turtle.done()