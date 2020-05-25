import turtle
l=turtle.Screen()
b=turtle.Turtle()
c=["red","green","yellow","purple","orange","cyan"]
b.speed(20)
for i in range(30):
    b.pencolor(c[i%6])
    b.circle(5*i)
    b.circle(-5*i)
    b.left(i)
turtle.done()