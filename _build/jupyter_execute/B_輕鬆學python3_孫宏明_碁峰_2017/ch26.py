# ch26 物件和類別

## 26-1 結構化程式設計和物件導向程式設計

# %load "26-1/main.py"
# 載入math套件，我們要用它的圓周率pi值
import math

# 把圓的半徑儲存在一個list資料組
circle_radius = [1, 2, 3, 4, 5]

print('\n圓面積: ', end='')
for radius in circle_radius:
  area = math.pi * radius * radius   # 計算圓面積的公式

  # 利用字串物件的format()方法設定取2位小數
  print('{:.2f}'.format(area), end=' ')

print('\n圓周長: ', end='')
for radius in circle_radius:
  perimeter = 2 * math.pi * radius   # 計算圓周長度的公式

  # 利用字串物件的format()方法設定取2位小數
  print('{:.2f}'.format(perimeter), end=' ')

## 26-3 實作物件導向程式專案

# %load "26-3/Graph/main.py"
# 載入shape套件
import shape as sh

circle_radius = [1, 2, 3, 4, 5]
circles = []   # 儲存Circle物件的資料組

# 用for迴圈建立5個Circle物件，把它們存入circles資料組
for radius in circle_radius:
    c = sh.Circle(radius)
    circles += [c]

# 顯示Circle物件的面積
print('\n圓面積: ', end='')
for c in circles:
    # 利用字串物件的format()方法設定取2位小數
    print('{:.2f}'.format(c.get_area()), end=' ')

# 顯示Circle物件的周長
print('\n圓周長: ', end='')
for c in circles:
    # 利用字串物件的format()方法設定取2位小數
    print('{:.2f}'.format(c.get_perimeter()), end=' ')


# %load "26-3/Graph/shape/circle.py"
# 載入math套件，我們要用它的圓周率pi值
import math


class Circle:
  # 建構式的第二個參數是用來接收傳入的半徑
  def __init__(self, radius):
    # 利用self參數建立儲存資料的變數
    # 然後把半徑存入這個變數
    self._radius = radius

  # 這個方法用來取得半徑
  def get_radius(self):
    return self._radius  # 傳回類別內部變數的值

  # 這個方法用來設定半徑，第二個參數用來傳入半徑
  def set_radius(self, radius):
    self._radius = radius  # 把半徑存入類別內部的變數

  # 這個方法用來取得圓面積
  def get_area(self):
    # 利用類別內部的變數計算圓面積，然後傳回結果
    return math.pi * self._radius * self._radius

  # 這個方法用來取得圓周長度
  def get_perimeter(self):
    # 利用類別內部的變數計算圓周長度，然後傳回結果
    return 2 * math.pi * self._radius

