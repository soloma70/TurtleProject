import turtle
from random import choice, randint

window = turtle.Screen()
window.title('Пинг Понг')
window.setup(width=0.8, height=0.8)
window.bgcolor('black')
window.tracer(2)

# Рисование игрового поля
border = turtle.Turtle()
border.speed(0)
border.color('green')
border.begin_fill()
border.goto(-500,300)
border.goto(500,300)
border.goto(500,-300)
border.goto(-500,-300)
border.goto(-500,300)
border.end_fill()

# Рисование сетки посередине
border.goto(0,300)
border.color('white')
border.pensize(3)
border.setheading(270)
for i in range(25):
    if i%2==0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()
border.hideturtle()

# Рисование левой ракетки
rocket_a = turtle.Turtle()
rocket_a.speed(0)
rocket_a.color('white')
rocket_a.shape('square')
rocket_a.shapesize(stretch_len=1, stretch_wid=5)
rocket_a.penup()
rocket_a.goto(-450,0)

# Перемещение левой ракетки
def move_up_a():
    y = rocket_a.ycor() + 10
    if y > 250:
        y = 250
    rocket_a.sety(y)

def move_down_a():
    y = rocket_a.ycor() - 10
    if y < -250:
        y = -250
    rocket_a.sety(y)

# Рисование правой ракетки
rocket_b = turtle.Turtle()
rocket_b.speed(0)
rocket_b.color('white')
rocket_b.shape('square')
rocket_b.shapesize(stretch_len=1, stretch_wid=5)
rocket_b.penup()
rocket_b.goto(450,0)

# Перемещение правой ракетки
def move_up_b():
    y = rocket_b.ycor() + 10
    if y > 250:
        y = 250
    rocket_b.sety(y)

def move_down_b():
    y = rocket_b.ycor() - 10
    if y < -250:
        y = -250
    rocket_b.sety(y)

# Создание мячика
ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
#ball.speed(0)
ball.dx = 5
ball.dy = 5
ball.penup()

# Слежение за нажатиями
window.listen()
window.onkeypress(move_up_a, 'w')
window.onkeypress(move_down_a, 's')
window.onkeypress(move_up_b, 'Up')
window.onkeypress(move_down_b, 'Down')

# Логика движения мячика
while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.dy = - ball.dy

    if ball.xcor() >= 490 or ball.xcor() <= -490:
        ball.goto(0, randint(-200,200))
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])

    if ball.ycor() >= rocket_b.ycor()-50 and ball.ycor() <= rocket_b.ycor()+50 and ball.xcor() >= rocket_b.xcor()-20 \
            and ball.xcor() <= rocket_b.xcor()+20:
        ball.dx = -ball.dx

    if ball.ycor() >= rocket_a.ycor()-50 and ball.ycor() <= rocket_a.ycor()+50 and ball.xcor() >= rocket_a.xcor()-20 \
            and ball.xcor() <= rocket_a.xcor()+20:
        ball.dx = -ball.dx



window.mainloop()