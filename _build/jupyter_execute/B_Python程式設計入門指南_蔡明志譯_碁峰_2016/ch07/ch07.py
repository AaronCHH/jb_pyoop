# Ch07 物件與類別


## 7.2 定義物件類別

# %load Circle.py
import math 

class Circle:
    # Construct a circle object 
    def __init__(self, radius = 1):
        self.radius = radius

    def getPerimeter(self):
        return 2 * self.radius * math.pi

    def getArea(self):
        return self.radius * self.radius * math.pi
          
    def setRadius(self, radius):
        self.radius = radius

# %load TestCircle.py
from Circle import Circle

def main():
    # Create a circle with radius 1
    circle1 = Circle()
    print("The area of the circle of radius",
        circle1.radius, "is", circle1.getArea())

    # Create a circle with radius 25
    circle2 = Circle(25)
    print("The area of the circle of radius",
        circle2.radius, "is", circle2.getArea())

    # Create a circle with radius 125
    circle3 = Circle(125)
    print("The area of the circle of radius",
        circle3.radius, "is", circle3.getArea())

    # Modify circle radius
    circle2.radius = 100
    print("The area of the circle of radius", 
        circle2.radius, "is", circle2.getArea())

main() # Call the main function


## 7.3 類別圖

# %load TV.py
class TV:
    def __init__(self):
        self.channel = 1  # Default channel is 1
        self.volumeLevel = 1  # Default volume level is 1
        self.on = False  # By default TV is off
  
    def turnOn(self):
        self.on = True
  
    def turnOff(self):
        self.on = False
  
    def getChannel(self):
        return self.channel

    def setChannel(self, channel):
        if self.on and 1 <= self.channel <= 120:
            self.channel = channel
  
    def getVolumeLevel(self):
        return self.volumeLevel

    def setVolume(self, volumeLevel):
        if self.on and \
              1 <= self.volumeLevel <= 7:
            self.volumeLevel = volumeLevel
  
    def channelUp(self):
        if self.on and self.channel < 120:
            self.channel += 1
  
    def channelDown(self):
        if self.on and self.channel > 1:
            self.channel -= 1
  
    def volumeUp(self):
        if self.on and self.volumeLevel < 7:
            self.volumeLevel += 1
  
    def volumeDown(self):
        if self.on and self.volumeLevel > 1:
            self.volumeLevel -= 1


# %load TestTV.py
from TV import TV

def main():
    tv1 = TV()
    tv1.turnOn()
    tv1.setChannel(30)
    tv1.setVolume(3)
    
    tv2 = TV()
    tv2.turnOn()
    tv2.channelUp()
    tv2.channelUp()
    tv2.volumeUp()
    
    print("tv1's channel is", tv1.getChannel(), 
        "and volume level is", tv1.getVolumeLevel())
    print("tv2's channel is", tv2.getChannel(),
        "and volume level is", tv2.getVolumeLevel())

main() # Call the main function


## 7.4 不可變更物件與可變更物件

# %load TestPassMutableObject.py
from Circle import Circle 

def main():
    # Create a Circle object with radius 1
    myCircle = Circle()

    # Print areas for radius 1, 2, 3, 4, and 5.
    n = 5
    printAreas(myCircle, n)

    # Display myCircle.radius and times
    print("\nRadius is", myCircle.radius)
    print("n is", n)
  
# Print a table of areas for radius 
def printAreas(c, times):
    print("Radius \t\tArea")
    while times >= 1:
        print(c.radius, "\t\t", c.getArea())
        c.radius = c.radius + 1
        times -= 1

main() # Call the main function


## 7.5 隱藏資料項目

# %load CircleWithPrivateRadius.py
import math 

class Circle:
    # Construct a circle object 
    def __init__(self, radius = 1):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def getArea(self):
        return self.__radius * self.__radius * math.pi

## 類別的萃取與封裝

# %load TestLoanClass.py
from Loan import Loan

def main():
    # Enter yearly interest rate
    annualInterestRate = eval(input
        ("Enter yearly interest rate, for example, 7.25: "))

    # Enter number of years
    numberOfYears = eval(input(
        "Enter number of years as an integer: "))

    # Enter loan amount
    loanAmount = eval(input(
        "Enter loan amount, for example, 120000.95: "))

    # Enter a borrwer
    borrower = input("Enter a borrower's name: ")

    # Create a Loan object
    loan = Loan(annualInterestRate, numberOfYears, 
        loanAmount, borrower)

    # Display loan date, monthly payment, and total payment
    print("The loan is for", loan.getBorrower())
    print("The monthly payment is", format(
        loan.getMonthlyPayment(), '.2f'))
    print("The total payment is", format(
        loan.getTotalPayment(), '.2f'))

main() # Call the main function


## 物件導向思維

# %load UseBMIClass.py
from BMI import BMI

def main():
    bmi1 = BMI("John Doe", 18, 145, 70)
    print("The BMI for", bmi1.getName(), "is",
        bmi1.getBMI(), bmi1.getStatus())
    
    bmi2 = BMI("Peter King", 50, 215, 70)
    print("The BMI for", bmi2.getName(), "is",
        bmi2.getBMI(), bmi2.getStatus())

main() # Call the main function


## Others

# %load GeometricObject.py
class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled
  
    def __str__(self):
        return "color: " + self.__color + \
            " and filled: " + str(self.__filled)


# %load CircleFromGeometricObject.py
from GeometricObject import GeometricObject
import math

class Circle(GeometricObject):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def getArea(self):
        return self.__radius * self.__radius * math.pi
  
    def getDiameter(self):
        return 2 * self.__radius
  
    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def printCircle(self):
        print(self.__str__() + " radius: " + str(self.__radius))


# %load InvalidRadiusException.py
class InvalidRadiusException(RuntimeError):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius


# %load CircleWithCustomException.py
from GeometricObject import GeometricObject
from InvalidRadiusException import InvalidRadiusException 
import math

class Circle(GeometricObject):
    def __init__(self, radius):
        super().__init__()
        self.setRadius(radius)

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        if radius >= 0:
            self.__radius = radius
        else:
            raise InvalidRadiusException(radius)

    def getArea(self):
        return self.__radius * self.__radius * math.pi
  
    def getDiameter(self):
        return 2 * self.__radius
  
    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def printCircle(self):
        print(self.__str__(), "radius:", self.__radius)


# %load CircleWithException.py
from GeometricObject import GeometricObject
import math

class Circle(GeometricObject):
    def __init__(self, radius):
        super().__init__()
        self.setRadius(radius)

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        if radius < 0:
            raise RuntimeError("Negative radius")
        else:
            self.__radius = radius

    def getArea(self):
        return self.__radius * self.__radius * math.pi
  
    def getDiameter(self):
        return 2 * self.__radius
  
    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def printCircle(self):
        print(self.__str__() + " radius: " + str(self.__radius))


# %load CircleWithPrivateRadius.py
import math 

class Circle:
    # Construct a circle object 
    def __init__(self, radius = 1):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def getArea(self):
        return self.__radius * self.__radius * math.pi

