'''
#Exercise1
from turtle import *
import random
class Square(Turtle):
    def __init__ (self, size, color):
        Turtle.__init__(self)
        self.size = size
        self.color(color)
        self.shape("square")
        self.shapesize(size * size)
    def random_color (self):
        colors = ["red", "blue", "green", "yellow", "oreng", "pink", "bblack"]
        x = random.randint(0, 6)
        self.color(colors[x])
        print(colors[x])
        

square1 = Square(3, 'red')

square1.random_color()
'''


#Exercise2
from turtle import *
import random
class hexagon (Turtle):
    def __init__(self, color, speed):
        Turtle.__init__(self)
        self.color(color)
        self.speed(speed)
    def Hexagon (self):
        self.begin_poly()
        self.fd(100)
        self.left(60)
        self.fd(100)
        self.left(60)
        self.fd(100)
        self.left(60)
        self.fd(100)
        self.left(60)
        self.fd(100)
        self.left(60)
        self.fd(100)
        self.end_poly()
        register_shape("hexagon", self.get_poly())
        self.shape("hexagon")
Hex = hexagon("red", 10)
Hex.Hexagon()


#Exerice3
#I added speed to the hexagon
