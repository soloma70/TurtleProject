import turtle

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

ball = turtle.Turtle(shape='circle')
ball.hideturtle()
ball.up()
ball.goto(0,200)
ball.speed_y = 0
ball.speed_x = 2
ball.showturtle()

gravity = 0.1

while True:
    ball.speed_y = ball.speed_y - gravity
    ball.goto(ball.xcor()+ball.speed_x, ball.ycor()+ball.speed_y)

    if ball.ycor() <= -240:
        ball.speed_y = -ball.speed_y
    if ball.xcor() >= 240 or ball.xcor() <= -240:
        ball.speed_x = -ball.speed_x

windows.mainloop()