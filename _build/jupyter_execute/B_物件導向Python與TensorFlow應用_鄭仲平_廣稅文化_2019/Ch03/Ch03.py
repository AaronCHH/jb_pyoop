# Ch03 類別

## 3.2 如何產生物件

# %load ex03-01.py
class Rose():
  price = 10.25
  month = 10

  def say(self):
    print("Color is RED")


if __name__ == '__main__':
  rose = Rose()
  rose.say()

## 3.3 Object Reference

# %load ex03-02.py
class Rose():
  price = 0
  month = 0

  def __init__(self, p, m):
    self.price = p
    self.month = m

  def get_month(self):
    return self.month


if __name__ == '__main__':

  def display(x):
    print("Month:", x.get_month())

  r1 = Rose(10.25, 10)
  r2 = Rose(8.5, 6)

  display(r1)
  display(r2)

# %load ex03-03.py
class Rose():
  price = 0
  month = 0

  def __init__(self, p, m):
    self.price = p
    self.month = m

  def get_month(self):
    return self.month


if __name__ == '__main__':

  def create_object():
    r = Rose(8.28, 3)
    return r

  rose = create_object()

  print("Month:", rose.get_month())

## 3.4 Constructor

# %load ex03-04.py
class Rose():
  price = 0
  month = 0

  def __init__(self, p, m):
    self.price = p
    self.month = m

  def get_month(self):
    return self.month


if __name__ == '__main__':
  rose = Rose(8.28, 3)
  print("Month:", rose.get_month())

## 3.5 子類別

# %load ex03-05.py
class Person():
  def __init__(self, na, a):
    self.name = na
    self.age = a

  def birth_year(self):
    return 2019 - self.age

  def display(self):
    print("Name:", self.name, "B.Year:", self.birth_year())


class Teacher(Person):
  def __init__(self, na, a, s):
    super().__init__(na, a)
    self.salary = s

  def display(self):
    super().display()
    print("Salary:", self.salary)


if __name__ == '__main__':
  tr = Teacher("Steven:", 20, 35000)
  tr.display()