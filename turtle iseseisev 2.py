import turtle
import random
aken = turtle.Screen()
aken.setup(600,600)
aken.bgcolor("pink")
k = turtle.Turtle()
def kolmnurk():
    for i in range(3):
        k.fd(50)
        k.rt(120)
    k.rt(60)
for i in range(6):
    kolmnurk()