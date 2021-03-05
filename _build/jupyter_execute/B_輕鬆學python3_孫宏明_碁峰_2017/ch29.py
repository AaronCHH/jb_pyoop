# ch29 多型

## 29-1 多型

# %load "29-1/Graph/shape/circle.py"
# 載入math模組，我們要使用它的pi值
import math


class Circle:
  def __init__(self, radius):
    self.__radius = radius

  def show_shape_info(self):
    print('圓形，半徑' + str(self.__radius))

  def get_area(self):
    return math.pi * self.__radius * self.__radius

# %load "29-1/Graph/shape/rectangle.py"
class Rectangle:
  def __init__(self, length, width):
    self.__length = length
    self.__width = width

  def show_shape_info(self):
    print('矩形，長' + str(self.__length) + '，'
          + '寬' + str(self.__width))

  def get_area(self):
    return self.__length * self.__width

# %load "29-1/Graph/shape/triangle.py"
class Triangle:
  def __init__(self, bottom, height):
    self.__bottom = bottom
    self.__height = height

  def show_shape_info(self):
    print('三角形，底' + str(self.__bottom) + '，'
          + '高' + str(self.__height))

  def get_area(self):
    return self.__bottom * self.__height / 2

# %load "29-1/Graph/main.py
import shape as sh

# 建立Circle、Rectangle和Triangle類別的物件
c = sh.Circle(10)
r = sh.Rectangle(5, 2)
t = sh.Triangle(8, 3)

# 把物件加入Tuple資料組
shapes = c, r, t

# 用For迴圈顯示每一個物件的內容和面積
for s in shapes:
  s.show_shape_info()
  print('面積：' + str(s.get_area()))

## 29-2 用繼承實作多型

# %load "29-2/Graph2/shape/shapeobject.py"
class ShapeObject:
  def show_shape_info(self):
    raise NotImplementedError(
      '子類別必須覆寫show_shape_info()方法')

  def get_area(self):
    raise NotImplementedError(
      '子類別必須覆寫get_area()方法')

# %load "29-2/Graph2/shape/circle.py"
from shape.shapeobject import *
import math   # 載入math模組，我們要使用它的pi值


class Circle(ShapeObject):
  def __init__(self, radius):
    self.__radius = radius

  def show_shape_info(self):
    print('圓形，半徑' + str(self.__radius))

  def get_area(self):
    return math.pi * self.__radius * self.__radius

# %load "29-2/Graph2/shape/rectangle.py"
from shape.shapeobject import *


class Rectangle(ShapeObject):
  def __init__(self, length, width):
    self.__length = length
    self.__width = width

  def show_shape_info(self):
    print('矩形，長' + str(self.__length) + '，'
          + '寬' + str(self.__width))

  def get_area(self):
    return self.__length * self.__width

# %load "29-2/Graph2/shape/triangle.py"
from shape.shapeobject import *


class Triangle(ShapeObject):
  def __init__(self, bottom, height):
    self.__bottom = bottom
    self.__height = height

  def show_shape_info(self):
    print('三角形，底' + str(self.__bottom) + '，'
          + '高' + str(self.__height))

  def get_area(self):
    return self.__bottom * self.__height / 2

# %load "29-2/Graph2/main.py"
import shape as sh

# 建立Circle、Rectangle和Triangle類別的物件
c = sh.Circle(10)
r = sh.Rectangle(5, 2)
t = sh.Triangle(8, 3)

# 把物件加入Tuple資料組
shapes = c, r, t

# 用For迴圈顯示每一個物件的內容和面積
for s in shapes:
  s.show_shape_info()
  print('面積：' + str(s.get_area()))

