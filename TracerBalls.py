import turtle
import random

window = turtle.Screen()
window.bgcolor('green')


border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.pensize(10)
border.up()
border.goto(-250, 250)
border.down()
border.goto(-250, -250)
border.goto(250, -250)
border.goto(250, 250)
window.tracer(10)

balls = []
count = 30
forms = ['circle', 'square', 'triangle', 'turtle']

for i in range(count):
    ball = turtle.Turtle(shape=random.choice(forms))
    red = random.random()
    green = random.random()
    blue = random.random()
    ball.color(red, green, blue)
    ball.hideturtle()
    ball.up()
    ball.goto(random.randint(-200,200), random.randint(50,250))
    ball.speed_y = 0
    ball.speed_x = random.randint(-3,3)
    ball.angle = random.randint(-5,5)
    ball.gravity = random.randint(1,30) * 0.01
    ball.showturtle()
    balls.append(ball)


while True:
    window.update()
    for ball in balls:
        ball.left(ball.angle)
        ball.speed_y = ball.speed_y - ball.gravity
        ball.goto(ball.xcor()+ball.speed_x, ball.ycor()+ball.speed_y)

        if ball.ycor() <= -240:
            ball.sety(-240)
            ball.speed_y = -ball.speed_y
        if ball.xcor() >= 240 or ball.xcor() <= -240:
            ball.speed_x = -ball.speed_x

windows.mainloop()

