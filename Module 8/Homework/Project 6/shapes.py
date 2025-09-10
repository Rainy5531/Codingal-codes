import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.setup(700, 700)
s.title("Equilateral Triangle, Rectangle, and Hexagon")
s.bgcolor("Black")
t.hideturtle()

while True:
    # Equilateral Triangle
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    t.width(3)
    t.color("lime")
    t.fillcolor("red")
    t.begin_fill()
    for _ in range(3):
        t.forward(150)
        t.left(120)
    t.end_fill()

    # Rectangle
    t.penup()
    t.goto(50, 100)
    t.pendown()
    t.width(3)
    t.color("magenta")
    t.fillcolor("yellow")
    t.begin_fill()
    for _ in range(2):
        t.forward(200)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()

    # Hexagon
    t.penup()
    t.goto(-75, -150)
    t.pendown()
    t.width(3)
    t.color("orange")
    t.fillcolor("blue")
    t.begin_fill()
    for _ in range(6):
        t.forward(100)
        t.left(60)
    t.end_fill()