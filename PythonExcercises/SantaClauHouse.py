import math
import turtle

turn = 90

turtle.forward(100)
turtle.left(turn)
turtle.forward(100)
turtle.left(turn)
turtle.forward(100)
turtle.left(turn)
turtle.forward(100)

a = 100

b = 100

c = math.sqrt(a**2+b**2)

turtle.left(135)
turtle.forward(c)
turtle.left(turn)
turtle.forward(c/2)
turtle.left(turn)
turtle.forward(c/2)
turtle.left(turn)
turtle.forward(c)
