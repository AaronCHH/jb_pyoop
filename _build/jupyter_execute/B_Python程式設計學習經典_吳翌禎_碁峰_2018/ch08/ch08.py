# Python 基本語法：物件導向

## 8.1 物件導向概念

# %load MyClass.py
# -------------------------------
#   Car.py
# -------------------------------
class Car:
  def __init__(self, brand, model, seats, cc):
    self.brand = brand
    self.model = model
    self.seats = seats
    self.cc = cc

  def display(self):
    s = "品牌:"+self.brand + "\r\n"
    s = s + "型號:" + self.model + "\r\n"
    s = s + "規格:" + self.seats + "座位" + self.cc + "CC"
    return s

## 8.2 類別與物件

# %load CH_8_2_EX_1_Class_Definition.py
# -----------------------------------
#  CH_8_2_EX_1_Class_Definition.py
# -----------------------------------
class Human:
  def __init__(self, height, weight):
    self.height = height
    self.weight = weight

  def BMI(self):
    return self.weight / ((self.height/100)**2)

# %load CH_8_2_EX_2_Object_Creation_1.py
# -------------------------------------
#   CH_8_2_EX_2_Object_Creation_1.py
# -------------------------------------
class Human:
  def __init__(self, height, weight):
    self.height = height
    self.weight = weight

  def BMI(self):
    return self.weight / ((self.height/100)**2)


# 建立物件
model_Bill = Human(180, 88)

# 印出物件兩個屬性
print(model_Bill.height)
print(model_Bill.weight)

# 使用物件方法
print(model_Bill.BMI())

# %load CH_8_2_EX_3_Object_Creation_2.py
# -------------------------------------
#   CH_8_2_EX_3_Object_Creation_2.py
# -------------------------------------
class Car:
  def __init__(self, brand, model, seats, cc):
    self.brand = brand
    self.model = model
    self.seats = seats
    self.cc = cc

  def display(self):
    s = "品牌:"+self.brand + "\r\n"
    s = s + "型號:" + self.model + "\r\n"
    s = s + "規格:" + self.seats + "座位" + self.cc + "CC"
    return s


# 建立物件
mycar1 = Car("Nissan", "X Trail", "4", "2400")

# 使用物件方法
print(mycar1.display())

## 8.3 繼承

# %load CH_8_3_EX_1_Inheritance.py
# -------------------------------
#   CH_8_3_EX_1_Inheritance.py
# -------------------------------
class Car:
  def __init__(self, brand, model, seats, cc):
    self.brand = brand
    self.model = model
    self.seats = seats
    self.cc = cc

  def display(self):
    s = "品牌:"+self.brand + "\r\n"
    s = s + "型號:" + self.model + "\r\n"
    s = s + "規格:" + self.seats + "座位" + self.cc + "CC"
    return s

# Truck類別繼承Car類別
class Truck(Car):
  pass

# %load CH_8_3_EX_2_Inheritance_Using_Override_Function.py
# -------------------------------------------------------
#   CH_8_3_EX_2_Inheritance_Using_Override_Function.py
# -------------------------------------------------------
from MyClass import Car


class Truck(Car):
  # -----新增loading載重屬性
  def __init__(self, brand, model, seats, cc, loading):

    # -----使用super()
    super().__init__(brand, model, seats, cc)
    self.loading = loading

# -----覆寫display()方法
  def display(self):
    s = "本卡車是" + self.brand + " "+self.model + "\r\n"
    s = s + self.cc + "CC" + "\r\n"
    s = s + "目前重量為" + self.loading + "噸" + "\r\n"
    return s


# -----建立物件
mycar1 = Car("Nissan", "X Trail", "4", "2400")
mytruck1 = Truck("Ford", "F-150", "2", "2700", "2.2")

# -----使用物件方法
print(mycar1.display())
print("-"*30)
print(mytruck1.display())

# %load CH_8_3_EX_2_Inheritance_Using_Super_Fuction.py
# ---------------------------------------------------
#   CH_8_3_EX_2_Inheritance_Using_Super_Fuction.py
# ---------------------------------------------------
from MyClass import Car


class Truck(Car):
  #----- 新增loading載重屬性
  def __init__(self, brand, model, seats, cc, loading):

    #----- 使用super()
    super().__init__(brand, model, seats, cc)
    self.loading = loading

## 8.4 封裝

# %load CH_8_4_EX_1_Encapsulation_1.py
# -----------------------------------
#   CH_8_4_EX_1_Encapsulation_1.py
# -----------------------------------
class Human:
  def __init__(self, height, weight):
    self.__height = height
    self.__weight = weight

  def BMI(self):
    return self.__weight / ((self.__height/100)**2)


# -----建立物件
model_Bill = Human(180, 88)

# -----使用物件方法
print(model_Bill.BMI())

# %load CH_8_4_EX_2_Encapsulation_2.py
# -----------------------------------
#   CH_8_4_EX_2_Encapsulation_2.py
# -----------------------------------
class Human:
  def __init__(self, height, weight):
    self.__height = height
    self.__weight = weight

  def BMI(self):
    return self.__weight / ((self.__height/100)**2)


# -----建立物件
model_Bill = Human(180, 88)

# -----印出物件兩個屬性
print(model_Bill.__height)
print(model_Bill.__weight)

## 8.3 多型

# %load CH_8_5_EX_1_ Polymorphism.py
# ---------------------------------
#   CH_8_5_EX_1_ Polymorphism.py
# ---------------------------------
class Mymath:
  def getArea(self, radiusorbase, height=None):
    if height is not None:
      return (radiusorbase * (height / 2))
    else:
      return (3.14 * (radiusorbase * radiusorbase))


# -----建立物件
obj = Mymath()

# -----輸入兩個參數呼叫方法計算三角形面積
print(obj.getArea(10, 10))

# -----輸入一個參數呼叫方法計算圓形面積
print(obj.getArea(5))

