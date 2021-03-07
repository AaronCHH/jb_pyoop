# Ch05 封裝(Encapsulation)

## 5.2 封裝(Encapsulation)

# %load ex05-01.py
class Tree():
  pass

if __name__ == '__main__':
    a = Tree
    print("Object is created")

# %load ex05-02.py
class Tree():
  def input(self, hei):
    self.variety = None
    self.age = None
    self.height = hei


if __name__ == '__main__':
  a = Tree()
  a.input(2.1)
  print("Set a.height to  ", a.height)

# %load ex05-03.py
class Tree():
  def input(self, hei):
    self.variety = None
    self.age = None
    self.height = hei

  def input(self, hei):
    self.height = hei

  def inquireHeight(self):
    return self.height


if __name__ == '__main__':
  a = Tree()
  a.input(2.1)
  h = a.inquireHeight()
  print("height = ", h, "公尺")

## 5.3 私有屬性與函數

# %load ex05-05.py
class Tree():
  def input(self, hei):
    self.variety = None
    self.age = None
    self.height = None

if __name__ == '__main__':
  a = Tree()
  a.height = 2.1
  print("Set a.height to ", a.height)

# %load ex05-07.py
class Tree():
  def input(self, hei):
    self.variety = None
    self.age = None
    self.__height = 2.1

if __name__ == '__main__':
  a = Tree()
  print("height = ", a.__height)

# %load ex05-08.py
class Tree():
  def input(self, hei):
    self.variety = None
    self.age = None
    self.__height = 2.1

  def input(self, hei):
    self.__height = hei

  def disp(self):
    print("height = ", a.__height)


if __name__ == '__main__':
  a = Tree()
  a.input(2.1)
  a.disp()


# %load ex05-10.py
class Tree():
  def input(self, hei):
    self.__variety = None
    self.__height = 2.1
    self.age = None

  def ShowAge(self):
    print("Age = ", self.age)


if __name__ == '__main__':
  a = Tree()
  a.age = 8
  a.age += 2
  a.ShowAge()


# %load ex05-11.py
class Tree():
  def input(self, v, a, hei):
    self.__variety = v
    self.__age = a
    self.__height = hei

  def Show(self):
    print(self.__variety, self.__age, self.__height)


if __name__ == '__main__':
  a = Tree()
  b = Tree()
  a.input("peach", 8, 2.1)
  b.input("pineapple", 2, 0.5)

  a.Show()
  b.Show()


## 5.4 類別層級屬性

# %load ex05-12.py
class Employee():
  temp = 0

  def __init__(self, na, sa):
    self.emp_name = na
    self.salary = sa

  def save_to_temp(self):
    Employee.temp = self.salary

  def load_from_temp(self):
    self.salary = Employee.temp

  def Display(self):
    print("Name=", self.emp_name, ", Salary:", self.salary)


if __name__ == '__main__':
  tom = Employee("Tom", 7777.25)
  peter = Employee("Peter", 1643.5)

  tom.save_to_temp()
  peter.load_from_temp()

  peter.Display()

# %load ex05-13.py
class Employee():
  counter = 0
  sum = 0

  def __init__(self, na, sa):
    self.emp_name = na
    self.salary = sa
    Employee.counter += 1
    Employee.sum += self.salary

  def Display_Avg(self):
    print("The number of employee:", Employee.counter)
    print("Average salary:", Employee.sum / Employee.counter)

  def Display(self):
    print("Name=", self.emp_name, ", Salary:", self.salary)


if __name__ == '__main__':
  e1 = Employee("Tom", 25000.0)
  e2 = Employee("Lily", 20000.0)
  e1.Display()
  e2.Display()
  e1.Display_Avg()

## 5.5 類別層級函數

# %load ex05-14.py
class Employee():
  counter = 0
  sum = 0

  @classmethod
  def NumberOfObject(cls):
    return cls.counter

  @classmethod
  def Average(cls):
    return cls.sum / cls.counter

  @classmethod
  def Display_Avg(cls):
    print("Average salary:", cls.Average())

  def __init__(self, na, sa):
    self.emp_name = na
    self.salary = sa
    Employee.counter += 1
    Employee.sum += self.salary

  def display(self):
    print("Number of Employee:", Employee.NumberOfObject())


if __name__ == '__main__':
  e1 = Employee("Tom", 25000.0)
  e2 = Employee("Lily", 20000.0)
  e1.display()
  Employee.Display_Avg()