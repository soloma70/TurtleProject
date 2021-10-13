import turtle, time, random

def star_fill(n, len):
    joe.left(random.randint(10, 350))
    joe.begin_fill()
    if n % 2 != 0:
        for i in range(n):
            joe.forward(len)
            angle = n // 2 * 360 / n
            joe.left(angle)
    joe.end_fill()

window = turtle.Screen()
window.bgcolor('black')
window.setup(700, 500)

joe = turtle.Turtle()
joe.speed(50)
joe.color('orange')
joe.hideturtle()

for i in range(5):
    x = random.randint(-320, 320)
    y = random.randint(-220, 220)
    joe.up()
    joe.setposition(x, y)
    joe.down()
    size = random.randint(10, 20)
    apex = random.choice([5, 7, 9, 11, 13, 15])
    star_fill(apex, size)

def move(x, y):
    joe.up()
    joe.setposition(x, y)
    joe.down()
    size = random.randint(10, 20)
    apex = random.choice([5, 7, 9])
    star_fill(apex, size)

window.onclick(move)
window.listen()
window.mainloop()

