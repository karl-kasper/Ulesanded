import turtle
import random
aken = turtle.Screen()
aken.setup(600,600)
aken.bgcolor("pink")
k = turtle.Turtle()
def ruut():
    k.lt(45)
    k.penup()
    k.fd(50)
    k.rt(90)
    k.pendown()
    for i in range(1):
        k.fd(50)
        for i in range(3):
            k.rt(90)
            k.fd(50)
            k.fd(50)
        k.rt(90)
        k.fd(50)
def ruudud():
    for i in range(2):
        k.speed(0)
        ruut()
        k.rt(90)
        k.penup()
        k.fd(50)
        k.pendown()
ruudud()
