print("day 0 homework")
from turtle import *
# we whant to paint a hou
colormode
def square(a, b):
    forward(a)
    left(90)
    forward(b)
    left(90)
    forward(a)
    left(90)
    forward(b)
    left(90)


def triangle(a):
    forward(a)
    left(120)
    forward(a)
    left(120)
    forward(a)
    left(120)


brown="#854325"
lightgreen="#c2dab8"
grey=(0.5, 0.5, 0.5)
lightgrey=(0.9, 0.9, 0.9)
babyblue="#89cff0"

bgcolor(lightgreen)

speed(50)

#house frame
color(grey)
width(4)

goto(0, -200)
begin_fill()
fillcolor(lightgrey)
square(200, 200)
end_fill()

#door
penup()
goto(75,-200)
pendown()

color(brown)
begin_fill()
square(50, 75)
end_fill()


penup()
goto(114, -165)
pendown()

color('black')
square(2, 2)


# window 1
color(brown)
width(5.5)
penup()
goto(125,-75)
pendown()

fillcolor(babyblue) 
begin_fill()
square(50, 50)


penup()
goto(25, -75)
pendown()

square(50, 50)
width(4)
end_fill()



#roof
penup()
goto(-10, 0)
pendown()

color('grey')
begin_fill()
triangle(220)
end_fill()

#window fream

color(brown)
penup()
goto(150, -25)


pendown()
right(90)
forward(50)

penup()
goto(125, -50)

pendown()
left(90)
forward(50)
penup()

goto(50, -25)
pendown()
right(90)
forward(50)

penup()
goto(25, -50)
left(90)
pendown()
forward(50)

#second roof
penup()
goto(3,0)
pendown()

color(lightgrey)
begin_fill()
fillcolor(lightgrey)
triangle(193)
end_fill()

#therd window
color(brown)
penup()
goto(100, 25)
pendown()
fillcolor(babyblue)
begin_fill()
circle(30)
end_fill()
left(90)
forward(60)

exitonclick()

