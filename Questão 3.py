import turtle

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Ponto({self.x}, {self.y})"

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()

ponto = Ponto(100, 50)

t.penup()
t.goto(ponto.x, ponto.y)
t.pendown()

t.dot(10, "red")

turtle.done()