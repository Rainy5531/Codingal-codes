import turtle

sc = turtle.Screen()
# creating canvas
sc.bgcolor("pink")

sc.setup(700, 700)

turtle.title("Welcome to Turtle Window")

# turtle object creation
board = turtle.Turtle()
board.fillcolor("yellow")
board.begin_fill()
n = 10
# creating a decagon
for i in range(0,n):
    board.forward(100)
    board.left(360/n)
board.end_fill()
turtle.done()