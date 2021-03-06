import turtle
import random

# Рисование границы
window = turtle.Screen()
border = turtle.Turtle()
border.speed(0)
border.hideturtle()
border.pensize(10)
border.color('red')

border.up()
border.goto(300,300)
border.down()
border.goto(300,-300)
border.goto(-300,-300)
border.goto(-300,300)
border.goto(300,300)

# Рисование мячика
ball = turtle.Turtle()
ball.hideturtle()
ball.shape('circle')
ball.up()
randx = random.randint(-290, 290)
randy = random.randint(-290, 290)
ball.goto(randx, randy)
ball.showturtle()

dx = 5
dy = 4
while True:
    x,y = ball.position()
    if x+dx >= 295 or x+dx <= -295:
        dx = -dx
    if y+dy >= 295 or y+dy <= -295:
        dy = -dy
    ball.goto(x+dx, y+dy)

window.mainloop()