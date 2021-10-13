import turtle

def move_up():
    x, y = pen.position()
    pen.setposition(x, y+speed)

def move_down():
    x, y = pen.position()
    pen.setposition(x, y-speed)

def move_left():
    x, y = pen.position()
    pen.setposition(x-speed, y)

def move_right():
    x, y = pen.position()
    pen.setposition(x+speed, y)

def change():
    if pen.isvisible():
        pen.up()
        pen.hideturtle()
    else:
        pen.down()
        pen.showturtle()

def speed_up():
    global speed
    speed += 1

def speed_down():
    global speed
    speed -= max(0, speed-1)

window = turtle.Screen()
pen = turtle.Turtle()
speed = 5

window.onkey(move_up, "Up")
window.onkey(move_down, "Down")
window.onkey(move_left, "Left")
window.onkey(move_right, "Right")
window.onkey(change, "space")
window.onkey(speed_up, "q")
window.onkey(speed_down, "w")

window.listen()
window.mainloop()