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

# Рисование мячиков
balls = []
count = 5
for i in range(count):
    ball = turtle.Turtle()
    ball.hideturtle()
    ball.shape('circle')
    ball.up()
    randx = random.randint(-270, 270)
    randy = random.randint(-270, 270)
    red = random.random()
    green = random.random()
    blue = random.random()
    ball.color(red, green, blue)
    ball.goto(randx, randy)
    ball.showturtle()
    dx = random.randint(-5, 5)
    dy = random.randint(-5, 5)
    balls.append([ball, dx, dy])


while True:
    for i in range(count):
        x,y = balls[i][0].position()
        if x+balls[i][1] >= 287 or x+balls[i][1] <= -287:
            balls[i][1] = -balls[i][1]
        if y+balls[i][2] >= 287 or y+balls[i][2] <= -287:
            balls[i][2] = -balls[i][2]
        balls[i][0].goto(x+balls[i][1], y+balls[i][2])

window.mainloop()