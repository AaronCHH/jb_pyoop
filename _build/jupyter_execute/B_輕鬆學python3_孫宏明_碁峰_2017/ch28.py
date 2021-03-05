# ch28 繼承

## 28-1 繼承

# %load "28-1/Inheritance/classes/parent.py"
class Parent:
  def __init__(self):
    self.public_var = 'Parent類別的公開變數'
    self._protected_var = 'Parent類別的保護變數'
    self.__private_var = 'Parent類別的私有變數'

  def public_method(self):
    return 'Parent類別的公開方法'

  def _protected_method(self):
    return 'Parent類別的保護方法'

  def __private_method(self):
    return 'Parent類別的私有方法'

# %load "28-1/Inheritance/classes/child.py"
from classes.parent import *


class Child(Parent):
  def __init__(self):
    super().__init__()

  # 這個方法會用到從父類別得到的公開變數public_var
  def get_super_public_var(self):
    return self.public_var

  # 這個方法會用到從父類別得到的保護變數protected_var
  def get_super_protected_var(self):
    return self._protected_var

  # 這個方法會用到從父類別得到的私有變數private_var
  def get_super_private_var(self):
    return self.__private_var

  # 這個方法會用到從父類別得到的公開方法public_method()
  def call_super_public_method(self):
    return self.public_method()

  # 這個方法會用到從父類別得到的保護方法protected_method()
  def call_super_protected_method(self):
    return self._protected_method()

  # 這個方法會用到從父類別得到的私有方法private_method()
  def call_super_private_method(self):
    return self.__private_method()

# %load "28-1/Inheritance/main.py"
from classes import *

s = Child()  # 建立Child類別的物件

# 呼叫六個公開的方法，觀察執行結果
# 其中有二個方法會發生例外錯誤
print(s.get_super_public_var())
print(s.get_super_protected_var())
# print(s.get_super_private_var())
print(s.call_super_public_method())
print(s.call_super_protected_method())
# print(s.call_super_private_method())

## 28-2 覆寫

# %load "28-2/Inheritance/classes/parent.py"
class Parent:
  def __init__(self):
    self.public_var = 'Parent類別的公開變數'
    self._protected_var = 'Parent類別的保護變數'
    self.__private_var = 'Parent類別的私有變數'

  def public_method(self):
    return 'Parent類別的公開方法'

  def _protected_method(self):
    return 'Parent類別的保護方法'

  def __private_method(self):
    return 'Parent類別的私有方法'

# %load "28-2/Inheritance/classes/child.py"
from classes.parent import *


class Child(Parent):
  def __init__(self):
    super().__init__()

    # 覆寫父類別的變數
    self.public_var = 'Child類別的公開變數'
    self._protected_var = 'Child類別的保護變數'

  def get_super_public_var(self):
    return self.public_var

  def get_super_protected_var(self):
    return self._protected_var

  def get_super_private_var(self):
    return self.__private_var

  def call_super_public_method(self):
    return self.public_method()

  def call_super_protected_method(self):
    return self._protected_method()

  def call_super_private_method(self):
    return self.__private_method()

  # 覆寫父類別的公開方法
  def public_method(self):
    return 'Child類別的公開方法'

  # 覆寫父類別的保護方法
  def _protected_method(self):
    return 'Child類別的保護方法'

# %load "28-2/Inheritance/main.py"
from classes import *

s = Child()  # 建立Child類別的物件

# 呼叫六個公開的方法，觀察執行結果
# 其中有二個方法會發生例外錯誤
print(s.get_super_public_var())
print(s.get_super_protected_var())
# print(s.get_super_private_var())
print(s.call_super_public_method())
print(s.call_super_protected_method())
# print(s.call_super_private_method())

## 28-3 多重繼承

# %load "28-3/Traffic/traffictools/car.py"
class Car:
  def __init__(self):
    self._name = 'Car'

  def show_name(self):
    print(self._name)

  def run(self):
    print('Running...')

  def stop(self):
    print('Stop')

# %load "28-3/Traffic/traffictools/airplane.py
class Airplane:
  def __init__(self):
    self._name = 'Airplane'

  def show_name(self):
    print(self._name)

  def take_off(self):
    print('Flying...')

  def land(self):
    print('Land')

# %load "28-3/Traffic/traffictools/flyingcar.py"
from traffictools.car import *
from traffictools.airplane import *


class FlyingCar(Airplane, Car):
  def __init__(self):
    super().__init__()

# %load "28-3/Traffic/main.py
from traffictools import *

# 建立一個FlyingCar物件
flyingcar = FlyingCar()

# 呼叫FlyingCar物件的方法
# 這些方法都是從父類別繼承得到的
flyingcar.show_name()
flyingcar.run()
flyingcar.stop()
flyingcar.take_off()
flyingcar.land()

