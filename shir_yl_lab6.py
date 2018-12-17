from turtle import *
import random
import math

class Ball(Turtle):
    def __init__(self, radius, color, speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed)

ball1 = Ball(20, "red", 100)
ball2 = Ball(20, "blue", 150)

ball1.penup()
ball1.goto(100,100)
ball1.pendown()

def random_color():
    r = random.randint (0,255)
    g = random.randint (0,255)
    b = random.randint (0,255)
    return r, g, b
screen.colormode(255)
screen.colormode()

def check_collision(ball1, ball2):
    radii = ball1.radius + ball2.radius

    x1 = ball1.pos()[0]
    x2 = ball1.pos()[1]
    y1 = ball2.pos()[0]
    y2 = ball2.pos()[0]
    r1 = ball1.radius
    r2 = ball2.radius

    d = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))
    r_sum = r1 + r2

    if r_sum >= d:
        ball1.color(random_color())
        ball2.color(random_color())
        print ("collision!")
    else:
        print ("not a collision")
check_collision(ball1, ball2)    
