import random
import turtle

billy=turtle.Turtle()

screen = turtle.Screen()

for i in range(0,99999999999):
    angle = random.randint(0, 360)
    billy.forward(100)
    billy.left(angle)

screen.mainloop()
