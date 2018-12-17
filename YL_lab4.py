#lab4


#problem1

#class Rectangle(object):
    #def __init__(self, width, height):
        #self.width = width
        #self.height = height
    #def Area(self):
        #return self.width * self.height
    #def Perimeter(self):
        #return (self.width + self.height) * 2
#rec1 = Rectangle(3, 4)

#print (rec1.Area())
#print (rec1.Perimeter())

#problem3

class Person():
    def __init__(self, name, age, city, gender):
        self.name = name
        self.age = age
        self.city = city
        self.gender = gender
    def eat(self, food):
        print('yum yum ' + self.name + ' ate ' + food)        
Shir = Person("Shir", "15", "Kfar_Yehoshua", "Female")
Yarden = Person("Yarden", "13", "Kfar_Yehoshua", "Female")
Maya = Person("Maya", "15", "Tivon", "Female")
Rotem = Person("Rotem", "15", "Shimshit", "male")
#print (Shir.name)
#print (Yarden.city)
#print (Maya.gender)
#print (Rotem.age)
Shir.eat('salad')
