# Ch07 物件導向程式開發

## 7.1 類別與物件

# %load class01.py
class Animal():  # 定義類別
  name = "小鳥"  # 定義屬性

  def sing(self):  # 定義方法
    print("很會唱歌!")


bird = Animal()  # 以 Animal 類別，建立一個名叫小鳥的 bird物件
print(bird.name)  # 小鳥
bird.sing()  # 很會唱歌!

# %load class02.py
class Animal():  # 定義類別
  def __init__(self, name):
    self.name = name  # 定義屬性

  def sing(self):  # 定義方法
    print(self.name + "，很會唱歌!")


bird = Animal("鸚鵡")  # 以 Animal 類別，建立一個名叫鸚鵡的 bird物件
print(bird.name)  # 鸚鵡
bird.sing()  # 鸚鵡，很會唱歌!

# %load class03.py
class Animal():  # 定義類別
  def __init__(self, name, age):
    self.name = name  # 定義屬性
    self.age = age

  def sing(self):  # 定義方法
    print(self.name + str(self.age) + "歲，很會唱歌!")

  def grow(self, year):  # 定義方法
    self.age += year


bird = Animal("鸚鵡", 1)  # 以 Animal 類別，建立一個名叫鸚鵡、1歲大的 bird物件
bird.grow(1)  # 長大1歲
bird.sing()  # 鸚鵡2歲，很會唱歌!

## 7.2 類別封裝

# %load class04.py
class Animal():  # 定義類別
  def __init__(self, name, age):
    self.__name = name  # 定義私用屬性
    self.__age = age

  def __sing(self):  # 定義私用方法
    print(self.__name + str(self.__age), end="歲，很會唱歌，")

  def talk(self):  # 定義共用方法
    self.__sing()  # 使用私用方法
    print("也會模仿人類說話!")


bird = Animal("灰鸚鵡", 2)  # 以 Animal 類別，建立一個名叫灰鸚鵡、2歲大的 bird物件
bird.talk()  # 灰鸚鵡2歲，很會唱歌，也會模仿人類說話!

bird.__age = -1  # 設定無效
bird.talk()  # 灰鸚鵡2歲，很會唱歌，也會模仿人類說話!
# bird.__sing()   #執行出現錯誤

## 7.3 類別繼承

# %load class05.py
class Animal():  # 定義父類別
  def __init__(self, name):
    self.name = name  # 定義共用屬性

  def fly(self):  # 定義共用方法
    print(self.name + "很會飛!")


class Bird(Animal):  # 定義子類別
  def __init__(self, name):
    self.name = "粉紅色" + name  # 覆寫父類別的建構式

  def sing(self):  # 定義子類別的方法
    print(self.name + "也愛唱歌!")


pigeon = Animal("小白鴿")  # 以 Animal 類別，建立一個名叫小白鴿的 pigeon 物件
pigeon.fly()  # 小白鴿很會飛!

parrot = Bird("小鸚鵡")  # 以 Bird 類別，建立一個名叫小鸚鵡的 parrot 物件
parrot.fly()  # 粉紅色小鸚鵡很會飛!
parrot.sing()  # 粉紅色小鸚鵡也愛唱歌!

# %load class06.py
class Animal():  # 定義父類別
  def __init__(self, name):
    self.name = name  # 定義共用屬性

  def fly(self):  # 定義共用方法
    print(self.name + "很會飛!")


class Bird(Animal):  # 定義子類別
  def __init__(self, name, age):
    super().__init__(name)  # 執行父類別的 __init__()方法
    self.age = age  # 定義子類別共用屬性

  def fly(self):  # 定義子類別共用方法
    print(str(self.age), end="歲")
    super().fly()  # 執行父類別的 fly方法


pigeon = Animal("小白鴿")  # 以 Animal 類別，建立一個名叫小白鴿的 pigeon 物件
pigeon.fly()  # 小白鴿很會飛!

parrot = Bird("小鸚鵡", 2)  # 以 Bird 類別，建立一個名叫小鸚鵡、2歲大的 parrot 物件
parrot.fly()  # 2歲小鸚鵡很會飛!

## 7.4 多型

# %load class07.py
class Animal():  # 定義父類別
  def fly(self):  # 定義共用方法
    print("時速 20公里!")


class Bird(Animal):  # 定義子類別
  def fly(self, speed):  # 定義共用方法
    print("時速 " + str(speed) + "公里!")


class Plane():  # 定義類別
  def fly(self):  # 定義共用方法
    print("時速 1000公里!")


def fly(speed):  # 定義函式
  print("時速 " + str(speed) + "英哩!")


animal = Animal()  # 以 Animal 類別建立 animal 物件
animal.fly()  # 時速 20公里!

bird = Bird()  # 以 Bird 類別建立 bird 物件
bird.fly(60)  # 時速 60公里!

plane = Plane()  # 以 Plane 類別建立 plane 物件
plane.fly()  # 時速 1000公里!

fly(5)  # 時速 5英哩!

## 7.5 多重繼承

# %load class08.py
class Father():  # 定義父類別
  def say(self):  # 定義共用方法
    print("明天會更好!")


class Mother():  # 定義父類別
  def say(self):  # 定義共用方法
    print("包容、尊重!")


class Child(Father, Mother):  # 定義子類別
  pass


child = Child()  # 建立 child 物件
child.say()  # 明天會更好!

## 7.6 類別應用

# %load Area.py
class Rectangle():  # 定義父類別
  def __init__(self, width, height):
    self.width = width  # 定義共用屬性
    self.height = height  # 定義共用屬性

  def area(self):  # 定義共用方法
    return self.width * self.height


class Triangle(Rectangle):  # 定義子類別
  def area2(self):  # 定義子類別的共用方法
    return (self.width * self.height)/2


triangle = Triangle(5, 6)  # 建立 triangle 物件
print("矩形面積=", triangle.area())  # 30
print("三角形面積=", triangle.area2())  # 15

## 7.7 建立 Python 專案

# %load projectHello/index.py
from mypackage.Hello import sayHello

sayHello()

# %load projectHello/mypackage/Hello.py
def sayHello():
  print("Hello")

## 7.8 打造自己的模組

# %load module-1.py
def add(n1,n2):
    return n1+n2
    
def sub(n1,n2):
    return n1-n2

print(add(5,2))  # 7
print(sub(5,2))  # 3

# %load calculate.py
def add(n1,n2):
    return n1+n2
    
def sub(n1,n2):
    return n1-n2

# %load getPrivateAttribute.py
class Father():      #定義父類別  
    def __init__(self,name):
        self.name = name    
        self.__eye="黑色" #定義私用屬性
    def getEye(self):    #定義共用方法傳回私用屬性
        return self.__eye
        
class Child(Father):      #定義子類別  
    def __init__(self,name,eye):
        super().__init__(name)
        self.eye=eye
        self.fatherEye=super().getEye() #取得私用屬性
      
joe = Child("小華","棕色") #建立子類別物件 joe
print(joe.name+"眼睛是"+joe.eye+"，他的父親則是"+joe.fatherEye)
# 執行結果：小華眼睛是棕色，他的父親則是黑色      

# %load module-2.py
import calculate  # 匯入 calculate 模組

print(calculate.add(5, 2))  # 7
print(calculate.sub(5, 2))  # 3

# %load module-3.py
from calculate import add, sub

print(add(5, 2))  # 7
print(sub(5, 2))  # 3

# %load module-4.py
from calculate import add

print(add(5, 2))  # 7
print(sub(5, 2))  # NameError: name 'sub' is not defined

# %load module-5.py
from calculate import *

print(add(5, 2))  # 7
print(sub(5, 2))  # 3

# %load module-6.py
from calculate import add as a

print(a(5, 2))  # 7

# %load module-7.py
import calculate as cal  # 匯入 calculate 模組，並取別名為 cal

print(cal.add(5, 2))  # 7
print(cal.sub(5, 2))  # 3

### 7.8.4 多模組

# %load projectArea/index.py
from areapackage.myClass import Triangle

triangle = Triangle(5,6) #建立 triangle 物件
print("矩形面積=",triangle.area())    #30
print("三角形面積=",triangle.area2()) #15

# %load projectArea/areapackage/myClass.py
class Rectangle():  # 定義父類別
  def __init__(self, width, height):
    self.width = width  # 定義共用屬性
    self.height = height  # 定義共用屬性

  def area(self):  # 定義共用方法
    return self.width * self.height


class Triangle(Rectangle):  # 定義子類別
  def area2(self):  # 定義子類別的共用方法
    return (self.width * self.height)/2

### 7.8.5 共用模組

# %load CallModule.py
from areapackage2.Rectangle import Rectangle
from areapackage2.Triangle import Triangle

triangle = Triangle(5, 6)  # 建立 triangle 物件
print("矩形面積=", triangle.area())  # 30
print("三角形面積=", triangle.area2())  # 15.0

# %load password.py

