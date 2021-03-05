# Ch12 物件導向程式設計

## 12.1 類別與物件

# %load class10.py
import math
class Circle:
    def __init__(self, radius = 1):
        self.radius = radius

    def setRadius(self, radius):
        self.radius = radius

    def getPerimeter(self):
        perimeter = 2 * self.radius * math.pi 
        return perimeter

    def getArea(self):
        area = self.radius * self.radius * math.pi
        return area

def main():
    circle1 = Circle()
    print('circle1: radius is %d, perimeter is %.2f'%(circle1.radius, 
                         circle1.getPerimeter()))
    print('circle1: radius is %d, area is %.2f'%(circle1.radius, circle1.getArea()))

    print()
    circle2 = Circle(5)
    print('circle2: radius is %d, perimeter is %.2f'%(circle2.radius, 
                        circle2.getPerimeter()))
    print('circle2: radius is %d, area is %.2f'%(circle2.radius, circle2.getArea()))

    print('\nAfter set radius to 10')
    circle2.setRadius(10)
    print('circle2: radius is %d, perimeter is %.2f'%(circle2.radius, 
                       circle2.getPerimeter()))
    print('circle2: radius is %d, area is %.2f'%(circle2.radius, circle2.getArea()))

main()

# %load class20.py
class Gpa:
    def __init__(self, name = 'Nancy', score = 60):
        self.name = name
        self.score = score

    def setName(self, name):
        self.name = name

    def setScore(self, score):
        self.score = score    

    def getGpa(self):
        if self.score >= 80:
            print('%s\'s GPA is A.'%(self.name))
        elif self.score >= 70:
            print('%s\'s GPA is B.'%(self.name))
        elif self.score >= 60:
            print('%s\'s GPA is C.'%(self.name))
        elif self.score >= 50:
            print('%s\'s GPA is D.'%(self.name))
        else:
            print('%s\'sGPA is F.'%(self.name))

def main():
    gpa0 = Gpa()
    gpa0.getGpa()
    gpa1 = Gpa('John', 82)
    gpa1.getGpa()
    print()
    gpa2 = Gpa('mary', 74)
    gpa2.getGpa()
    gpa3 = Gpa()
    gpa3.setName('Jennifer')
    gpa3.setScore(99)
    gpa3.getGpa()

main()

# %load circle.py
import math
class Circle:
    def __init__(self, radius = 1):
        self.radius = radius

    def setRadius(self, radius):
        self.radius = radius

    def getPerimeter(self):
        perimeter = 2 * self.radius * math.pi 
        return perimeter

    def getArea(self):
        area = self.radius * self.radius * math.pi
        return area

# %load testCircle.py
from circle import Circle
def main():
    circle1 = Circle()
    print('circle1: radius is %d, perimeter is %.2f'%(circle1.radius, 
      	           circle1.getPerimeter()))
    print('circle1: radius is %d, area is %.2f'%(circle1.radius, circle1.getArea()))
    print()

    circle2 = Circle(5)
    print('circle2: radius is %d, perimeter is %.2f'%(circle2.radius,  
                 circle2.getPerimeter()))
    print('circle2: radius is %d, area is %.2f'%(circle2.radius, circle2.getArea()))
    print('\nAfter set radius to 10')

    circle2.setRadius(10)
    print('circle2: radius is %d, perimeter is %.2f'%(circle2.radius, 
circle2.getPerimeter()))
    print('circle2: radius is %d, area is %.2f'%(circle2.radius, circle2.getArea()))
    
main()

# %load gpa.py
class Gpa:
    def __init__(self, name = 'Nancy', score = 60):
        self.name = name
        self.score = score

    def setName(self, name):
        self.name = name

    def setScore(self, score):
        self.score = score    

    def getGpa(self):
        if self.score >= 80:
            print('%s\'s GPA is A.'%(self.name))
        elif self.score >= 70:
            print('%s\'s GPA is B.'%(self.name))
        elif self.score >= 60:
            print('%s\'s GPA is C.'%(self.name))
        elif self.score >= 50:
            print('%s\'s GPA is D.'%(self.name))
        else:
            print('%s\'sGPA is E.'%(self.name))

# %load testGpa.py
from gpa import Gpa
def main():
    gpa0 = Gpa()
    gpa0.getGpa()
    gpa1 = Gpa('John', 82)
    gpa1.getGpa()
    print()
    gpa2 = Gpa('mary', 74)
    gpa2.getGpa()
    gpa3 = Gpa()
    gpa3.setName('Jennifer')
    gpa3.setScore(99)
    gpa3.getGpa()

main()

## 12.2 private 屬性

# %load dataWithPrivate.py
import math
class Circle:
    def __init__(self, radius = 1):
        self.__radius = radius

    def setRadius(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def getPerimeter(self):
        perimeter = 2 * self.__radius * math.pi 
        return perimeter

    def getArea(self):
        area = self.__radius * self.__radius * math.pi
        return area

def main():
    circle1 = Circle()
    print('circle1: radius is %d, perimeter is %.2f'%(circle1.getRadius(), circle1.getPerimeter()))
    print('circle1: radius is %d, area is %.2f'%(circle1.getRadius(), circle1.getArea()))

    print()
    circle2 = Circle(5)
    print('circle2: radius is %d, perimeter is %.2f'%(circle2.getRadius(), circle2.getPerimeter()))
    print('circle2: radius is %d, area is %.2f'%(circle2.getRadius(), circle2.getArea()))

    print('\nAfter set radius to 10')
    circle2.setRadius(10)
    print('circle2: radius is %d, perimeter is %.2f'%(circle2.getRadius(), circle2.getPerimeter()))
    print('circle2: radius is %d, area is %.2f'%(circle2.getRadius(), circle2.getArea()))
    
main()

## 12.3 繼承

# %load inheritance10.py
import math
class Shape:
    def __init__(self, xPoint = 0, yPoint = 0):
        self.__xPoint = xPoint
        self.__yPoint = yPoint

    def getPoint(self):
        return self.__xPoint, self.__yPoint

    def setPoint(self, xPoint, yPoint):
        self.__xPoint = xPoint
        self.__yPoint = yPoint

    def __str__(self):
        print('xPoint = %d, yPoint = %d'%(self.__xPoint, self.__yPoint))

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def getArea(self):
        return self.__radius * self.__radius * math.pi

    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def __str__(self):
        super().__str__()
        print('radius: %d'%(self.__radius))

class Rectangle(Shape):
    def __init__(self, width = 1, height = 1):
        super().__init__()
        self.__width = width
        self.__height = height

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        self.__width = width

    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        self.__height = height

    def getArea(self):
        return self.__width * self.__height

    def getPerimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        super().__str__()
        print('width: %d'%(self.__width))
        print('height: %d'%(self.__height))

def main():
    circle = Circle(5)
    circle.__str__()
    print('Perimeter: %.2f'%(circle.getPerimeter()))
    print('Area: %.2f'%(circle.getArea()))
    print()    
    
    rectangle= Rectangle(2, 6)
    rectangle.__str__()
    print('Perimeter: %.2f'%(rectangle.getPerimeter()))
    print('Area: %.2f'%(rectangle.getArea()))

main()

# %load shape.py
import math
class Shape:
    def __init__(self,  xPoint = 0,  yPoint = 0):
        self.__xPoint = xPoint
        self.__yPoint = yPoint

    def getPoint(self):
        return self.__xPoint, self.__yPoint

    def setPoint(self,  xPoint,  yPoint):
        self.__xPoint = xPoint
        self.__yPoint = yPoint

    def __str__(self):
        print('xPoint = %d, yPoint = %d'%(self.__xPoint, self.__yPoint))

# %load circleFromShape.py
from shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def getArea(self):
        return self.__radius * self.__radius * math.pi

    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def __str__(self):
        super().__str__()
        print('radius: %d'%(self.__radius))

# %load rectangleFromShape.py
import math
from shape import Shape

class Rectangle(Shape):
    def __init__(self, width = 1, height = 1):
        super().__init__()
        self.__width = width
        self.__height = height

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        self.__width = width
        
    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        self.__height = height

    def getArea(self):
        return self.__width * self.__height

    def getPerimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        super().__str__()
        print('width: %d'%(self.__width))
        print('height: %d'%(self.__height))

# %load triangleFromShape.py
from shape import Shape
import math

class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__()
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def getCoordinate(self):
        return self.__x1, self.__y1, self.__x2, self.__y2
    

    def setCoordinate(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def getArea(self):
        x, y = super().getPoint()
        s1 = math.sqrt((self.__x1-x)**2 + (self.__y1-y)**2)
        s2 = math.sqrt((self.__x2-self.__x1)**2 + (self.__y2-self.__y1)**2)
        s3 = math.sqrt((self.__x2-x)**2 + (self.__y2-y)**2)
        print('s1 = %d, s2 = %d, s3 = %d'%(s1, s2, s3))
        s = (s1 + s2 + s3) / 2
        area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
        return area

    def getPerimeter(self):
        x, y = super().getPoint()
        s1 = math.sqrt((self.__x1-x)**2 + (self.__y1-y)**2)
        s2 = math.sqrt((self.__x2-self.__x1)**2 + (self.__y2-self.__y1)**2)
        s3 = math.sqrt((self.__x2-x)**2 + (self.__y2-y)**2)
        print(s1, s2, s3)
        return s1+s2+s3

    def __str__(self):
        super().__str__()
        x , y = super().getPoint()
        print('(%d, %d), (%d, %d), (%d, %d)'
            %(x, y, self.__x1, self.__y1, self.__x2, self.__y2))

# %load testCircleAndRectangle.py
from circleFromShape import Circle
from rectangleFromShape import Rectangle

def main():
    circle = Circle(5)
    circle.__str__()
    print('Perimeter: %.2f'%(circle.getPerimeter()))
    print('Area: %.2f'%(circle.getArea()))
    print()    
    
    rectangle= Rectangle(2, 6)
    rectangle.__str__()
    print('Perimeter: %.2f'%(rectangle.getPerimeter()))
    print('Area: %.2f'%(rectangle.getArea()))
    print()

main()

# %load testCircleAndRectAndTri.py
from circleFromShape import Circle
from rectangleFromShape import Rectangle
from triangleFromShape import Triangle

def main():
    circle = Circle(5)
    circle.__str__()
    print('Perimeter: %.2f'%(circle.getPerimeter()))
    print('Area: %.2f'%(circle.getArea()))
    print()    
    
    rectangle = Rectangle(2, 6)
    rectangle.__str__()
    print('Perimeter: %.2f'%(rectangle.getPerimeter()))
    print('Area: %.2f'%(rectangle.getArea()))
    print()

    triangle = Triangle(3, 0, 3, 4)
    triangle.__str__()
    print('Perimeter: %.2f'%(triangle.getPerimeter()))
    print('Area: %.2f'%(triangle.getArea()))

main()

## 12.4 多型

# %load polymorphism.py
from circleFromShape import Circle
from rectangleFromShape import Rectangle

def main():
    circle = Circle(5)
    circle.__str__()
    displayPerimeter(circle)
    displayArea(circle)
    print()

    rectangle= Rectangle(2, 6)
    rectangle.__str__()
    displayPerimeter(rectangle)
    displayArea(rectangle) 
    print()   

def displayArea(obj):
    print('Area: %.2f'%(obj.getArea()))

def displayPerimeter(obj):
    print('Permiter: %.2f'%(obj.getPerimeter()))  
    
main()

## 12.5 isinstance 函式

# %load isInstance.py
from circleFromShape import Circle
from rectangleFromShape import Rectangle

def main():
    circle = Circle(5)
    rectangle= Rectangle(2, 6)

    print('Circle information')
    displayInform(circle)
    print()
    
    print('Rectangle information')
    displayInform(rectangle)
    print()

def displayInform(obj):
    print('Area: %.2f'%(obj.getArea()))
    print('Permiter: %.2f'%(obj.getPerimeter()))  
    if isinstance(obj, Circle):
        print('Radius: %d'%(obj.getRadius()))
    elif isinstance(obj, Rectangle):
        print('Width: %d'%(obj.getWidth()))
        print('Width: %d'%(obj.getHeight()))
        
main()

## 12.6 範例集錦

# %load program12-1.py
class Bmi:
    def __init__(self, weight = 170, height = 60):
        self.__weight = weight
        self.__height = height
        
    def getBmi(self):
        heightMeter = self.__height / 100
        bmi = self.__weight / (heightMeter * heightMeter)
        print('%.2f'%(bmi))
        if bmi < 18.5:
            print('Underweight')
        elif bmi < 25:
            print('Normal')
        elif bmi < 30:
            print('Overweight')
        else:
            print('Obses')

def main():
    John = Bmi(68, 185)
    print('John\'s BMI is : ', end = '')
    John.getBmi()
    print()

    Mary = Bmi(53, 172)
    print('Mary\'s BMI is : ', end = '')
    Mary.getBmi()
    print()

main()

# %load animalClass.py
class Animal:
    def __init__(self, name = 'Unknown'):
        self.__name = name

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def breed(self):
        return 'viviparous'

    def food(self):
        return 'meat'
    
class Duck(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def breed(self):
        return 'Oviparous'

    def food(self):
        return 'grass'

# %load testAnimalClass.py
from animalClass import Animal, Lion, Duck
    
def main():
    lionObj = Lion('Luke')
    print('Lion Object')
    print('Name: %s'%(lionObj.getName()))
    print('Breed: %s'%(lionObj.breed()))
    print('Food: %s'%(lionObj.food()))
    print()

    duckObj = Duck('Kiki')
    print('Duck object')
    print('Name: %s'%(duckObj.getName()))
    print('Breed: %s'%(duckObj.breed()))
    print('Food: %s'%(duckObj.food()))

main()

# %load animalClass2.py
class Animal:
    def __init__(self, name = 'Unknown'):
        self.__name = name

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def breed(self):
        return 'viviparous'

    def food(self):
        return 'meat'
    
class Duck(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def breed(self):
        return 'Oviparous'

    def food(self):
        return 'grass'

# %load testAnimalClass2.py
from animalClass import Animal, Lion, Duck

def main():
    lionObj = Lion('Luke')
    print('Lion Object')
    print('Name: %s'%(lionObj.getName()))
    displayInform(lionObj)
    print()

    duckObj = Duck('Kiki')
    print('Duck object')
    print('Name: %s'%(duckObj.getName()))
    displayInform(duckObj)
    print()
    
#Polymorphism
def displayInform(obj):    
    print('Breed: %s'%(obj.breed()))
    print('Food: %s'%(obj.food()))
    
main()

# %load animalClass6.py
class Animal:
    def __init__(self, name = 'Unknown'):
        self.__name = name

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def breed(self):
        return 'viviparous'

    def food(self):
        return 'meat'

    def sound(self):
        return 'hon-hon-hon'
    
class Duck(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def breed(self):
        return 'Oviparous'

    def food(self):
        return 'earthworm'

    def sound(self):
        return 'A-A-A'
    
class Sheep(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def breed(self):
        return 'viviparous'

    def food(self):
        return 'grass'

    def sound(self):
        return 'Bei-Bei-Bei'

# %load testAnimalClass6.py
from animalClass6 import Animal, Lion, Duck, Sheep

def main():
    lionObj = Lion('Luke')
    print('Lion Object')
    print('Name: %s'%(lionObj.getName()))
    displayInform(lionObj)
    print()

    duckObj = Duck('Kiki')
    print('Duck object')
    print('Name: %s'%(duckObj.getName()))
    displayInform(duckObj)
    print()

    sheepObj = Sheep('Nala')
    print('sheep object')
    print('Name: %s'%(sheepObj.getName()))
    displayInform(sheepObj)
    print()
    
#Polymorphism
def displayInform(obj):    
    print('Breed: %s'%(obj.breed()))
    print('Food: %s'%(obj.food()))
    
main()

# %load queueClass.py
class Queue:
    def __init__(self):
        self.__items = []

    def isEmpty(self):
        return len(self.__items) == 0

    def insert(self, value):
        self.__items.insert(len(self.__items)+1, value)
        print('%d is added in queue.'%(value))

    def delete(self):
        if self.isEmpty():
            return 'The queue is empty.'
        else:
            return self.__items.pop(0)
        
    def getSize(self):
        return len(self.__items)

# %load testQueue.py
from queueClass import Queue

queueObj = Queue()
for i in range(1, 6):
    queueObj.insert(i)

while not queueObj.isEmpty():
    print(queueObj.delete(), end = ' ')

