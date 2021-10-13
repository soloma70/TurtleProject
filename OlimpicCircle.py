import turtle
windows = turtle.Screen()

rad = 75
thick = 10

europe = turtle.Turtle()
africa = turtle.Turtle()
america = turtle.Turtle()
asia = turtle.Turtle()
australia = turtle.Turtle()

for i in [europe, africa, america, asia, australia]:
    i.up()

europe.goto(-2*rad, 2*rad)
africa.goto(0, 2*rad)
america.goto(2*rad, 2*rad)
asia.goto(-rad, rad)
australia.goto(rad, rad)

for i in [europe, africa, america, asia, australia]:
    i.down()
    i.pensize(thick)

europe.color('blue')
africa.color('black')
america.color('red')
asia.color('yellow')
australia.color('green')

for i in [europe, africa, america, asia, australia]:
    i.circle(rad)

windows.mainloop()

