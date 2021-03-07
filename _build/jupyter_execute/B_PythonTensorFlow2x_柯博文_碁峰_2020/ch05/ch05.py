# Ch05 OOP

# %load ch05-OOP/01-def1.py
#!/usr/bin/env
def fun1():
  print("this is function1")


fun1()

# %load ch05-OOP/02-def2.py
#!/usr/bin/env
def fun2(num):
  print("this is function2=" + str(num))


fun2(100)
fun2(num=200)

# %load ch05-OOP/03-def3.py
#!/usr/bin/env
__author__ = "Powen Ko, www.powenko.com"


def fun3(num1=0, num2=0):
  return (num1 * 2) + num2


print(fun3(1, 2))
print(fun3(num2=1, num1=2))
print(fun3(num2=1))
a = fun3()
print(a)


def fun4():
  return 1, 2


a, b = fun4()
print(a)
print(b)

# %load ch05-OOP/04-def4.py
#!/usr/bin/env
def fun3(n1, n2):
  print(str(n1) + "*" + str(n2) + "=" + str(n1 * n2))


x = 0
while x < 9:
  x = x + 1
  y = 1
  while y < 10:
    fun3(x, y)
    y = y + 1

# %load ch05-OOP/05-def5.py
#!/usr/bin/env
__author__ = "Powen Ko, www.powenko.com"
"""
def fun3(num1=0,num2=0):
    return (num1*2)+num2
"""
import MyFun

a = MyFun.fun3(1, 2)
print(a)

# %load ch05-OOP/06-class1.py
class MyClass(object):
  def __init__(self):
    print("hello")


g = MyClass()

# %load ch05-OOP/07-class2-init.py
class Myclass(object):
  def __init__(self, name):
    print("hello " + name)


g = Myclass(name="PowenKo")
# g1=Myclass(name="PowenKo")

# %load ch05-OOP/08-class3-fun.py
class MyClass(object):
  def __init__(self, name):
    print("hello "+str(name))

  def fun1(self):
    print("fun1")

  def fun3(self, num1=0, num2=0):
    return (num1 * 2) + num2


g = MyClass("Powen")
g.fun1()
print(g.fun3(1, 2))
print(g.fun3(num2=1, num1=2))

# %load ch05-OOP/09-class4-selfValue.py
class MyClass(object):
  mX = 1
  mY = 1

  def __init__(self, x, y):
    self.mX = x
    self.mY = y
    self.x1 = x

  def fun1(self):
    s = ""
    for x in range(self.mX, 10, 1):
      for y in range(self.mY, 10, 1):
        s = str(x) + "*" + str(y) + "=" + str(x * y)
        print(s)
    print(self.x1)


x = 1
g = MyClass(8, 8)
g.fun1()
print(g.mX)

# %load ch05-OOP/10-class5-selfdef.py
class MyClass(object):
  mX = 1
  mY = 1

  def __init__(self, x, y):
    self.mX = x
    self.mY = y

  def fun1(self):
    s = ""
    for x in range(self.mX, 10, 1):
      for y in range(self.mY, 10, 1):
        self.fun2(x, y)

  def fun2(self, x, y):
    s = str(x) + "*" + str(y) + "=" + str(x * y)
    print(s)


g = MyClass(8, 8)
g.fun1()

# %load ch05-OOP/11-class6-PubPri.py
class MyClass(object):
  mMyPub = 1
  __mMyPri = 1

  def __init__(self, x, y):
    self.mMyPub = x
    self.__mMyPri = y

  def funPub(self):
    print("fun1")

  def __funPri(self):
    print("fun2")


g = MyClass(7, 7)
print(g.mMyPub)
# print(g.__mMyPri)
g.funPub()
# g.__funPri()

# %load ch05-OOP/12-class7-import.py
from MyClass import MyClass

g = MyClass(8, 8)
g.fun1()

# %load ch05-OOP/13-class8-inheritance.py
class MyClass(object):
  def __init__(self, name):
    print("MyClass " + str(name))

  def fun1(self):
    print("MyClass -> fun1")


class MyClassChild(MyClass):
  def __init__(self, name):
    print("MyClassChild " + str(name))

  def fun2(self):
    print("MyClassChild -> fun2")


g = MyClassChild("Powen Ko")
g.fun1()
g.fun2()

# %load ch05-OOP/14-class9-2inheritance.py
#!/usr/bin/env
__author__ = "Powen Ko, www.powenko.com"


class MyClass(object):
  def fun1(self):
    print("MyClass -> fun1")


class MyClass2(object):
  def fun2(self):
    print("MyClass2 -> fun2")


class MyClassChild(MyClass, MyClass2):
  def __init__(self, name):
    print("MyClassChild " + str(name))

  def fun3(self):
    print("MyClassChild -> fun3")


g = MyClassChild("Powen Ko")
g.fun1()
g.fun2()
g.fun3()

# %load ch05-OOP/15-class10-inheritanceSuper.py
#!/usr/bin/env
__author__ = "Powen Ko, www.powenko.com"


class MyClass(object):
  def fun1(self):
    print("MyClass -> fun1")

  def fun2(self):
    print("MyClass -> fun2")


class MyClassChild(MyClass):
  def __init__(self, name):
    print("MyClassChild " + str(name))

  def fun2(self):
    try:
      super().fun2()  # 3.x
    except:
      super(MyClassChild, self).fun2()  # 2.7
    print("MyClassChild -> fun3")


g = MyClassChild("Powen Ko")
g.fun1()
g.fun2()

# %load ch05-OOP/38class10-inheritanceSuperValue.py
#!/usr/bin/env
__author__ = "Powen Ko, www.powenko.com"


class MyClass(object):
  value2 = 2
  value3 = 3

  def fun1(self):
    print("MyClass -> fun1")

  def fun2(self):
    print("MyClass -> fun2")
    self.value1 = 1


class MyClassChild(MyClass):
  value3 = 13

  def __init__(self, name):
    print("MyClassChild " + str(name))

  def fun2(self):
    try:
      super().fun2()  # 3.x
    except:
      super(MyClassChild, self).fun2()  # 2.7
    print("MyClassChild -> fun3")
    print(self.value1)
    print(self.value2)
    print(self.value3)
    print(super(MyClassChild, self).value3)


g = MyClassChild("Powen Ko")
g.fun1()
g.fun2()

# %load ch05-OOP/MyClass.py
class MyClass(object):
  mX = 1
  mY = 1

  def __init__(self, x, y):
    self.mX = x
    self.mY = y

  def fun1(self):
    s = ""
    for x in range(self.mX, 10, 1):
      for y in range(self.mY, 10, 1):
        self.fun2(x, y)

  def fun2(self, x, y):
    s = str(x) + "*" + str(y) + "=" + str(x * y)
    print(s)

# %load ch05-OOP/MyFun.py
#!/usr/bin/env
__author__ = "Powen Ko, www.powenko.com"


def fun3(num1=0, num2=0):
  return (num1 * 2) + num2