import turtle
import random
import time

def choose_random_color():
    red = random.random()
    green = random.random()
    blue = random.random()
    return red, green, blue

window = turtle.Screen()
bob = turtle.Turtle()

while True:
    window.bgcolor(choose_random_color())
    bob.color(choose_random_color())
    bob.forward(30)
    bob.left(30)
    time.sleep(1)

window.mainloop()