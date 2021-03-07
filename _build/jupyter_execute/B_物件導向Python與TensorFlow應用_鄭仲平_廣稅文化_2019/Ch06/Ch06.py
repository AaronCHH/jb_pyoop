# Ch06 繼承(Inheritance)

## 6.2 建立類別繼承

# %load ex06-01.py
class Person():
  def setValue(self, na, a):
    self.name = na
    self.age = a

  def birthYear(self):
    return 2019 - self.age

  def display(self):
    print("Name:", self.name, ", Age:", self.age)


if __name__ == '__main__':
  mike = Person()
  mike.setValue("Mike", 45)
  mike.display()
  print("BirthYear:", mike.birthYear())


# %load ex06-02.py
class Person():
  def setValue(self, na, a):
    self.name = na
    self.age = a

  def birthYear(self):
    return 2019 - self.age

  def display(self):
    print("Name:", self.name, ", Age:", self.age)


class Teacher(Person):
  pass


if __name__ == '__main__':
  steven = Teacher()
  steven.setValue("Steven", 45)
  steven.display()


# %load ex06-03.py
class Person():
  def setValue(self, na, a):
    self.name = na
    self.age = a

  def birthYear(self):
    return 2019 - self.age

  def display(self):
    print("Name:", self.name, ", Age:", self.age)


class Teacher(Person):
  def tr_setValue(self, na, a, sa):
    super().setValue(na, a)
    self.salary = sa

  def pr(self):
    super().display()
    print("Salary:", self.salary)


if __name__ == '__main__':
  steven = Teacher()
  steven.tr_setValue("Steven", 35, 35000)
  steven.pr()


# %load ex06-04.py
class Person():
  def setValue(self, na, a):
    self.name = na
    self.age = a

  def birthYear(self):
    return 2019 - self.age

  def display(self):
    print("Name:", self.name, ", Age:", self.age)


class Teacher(Person):
  def setValue(self, na, a, sa):
    super().setValue(na, a)
    self.salary = sa

  def pr(self):
    super().display()
    print("Salary:", self.salary)


class Student(Person):
  def setValue(self, na, a, no):
    super().setValue(na, a)
    self.student_number = no

  def pr(self):
    super().display()
    print("StudNo:", self.student_number)


if __name__ == '__main__':
  x = Person()
  x.setValue("Alvin", 32)
  y = Student()
  y.setValue("Tom", 36, 11138)
  x.display()
  y.pr()

# %load ex06-05.py
class Person():
  def __init__(self):
    self.name = None
    self.age = None

  def setValue(self, na, a):
    self.name = na
    self.age = a

  def birthYear(self):
    return 2019 - self.age

  def display(self):
    print("Name:", self.name, ", Age:", self.age)


class Teacher(Person):
  def setValue(self, na, a, sa):
    super().setValue(na, a)
    self.salary = sa

  def pr(self):
    super().display()
    print("Salary:", self.salary)


class Student(Person):
  def setValue(self, na, a, no):
    super().__init__()
    super().setValue(na, a)
    self.student_number = no

  def pr(self):
    super().display()
    print("StudNo:", self.student_number)


if __name__ == '__main__':
  x = Person()
  x.setValue("Alvin", 32)
  y = Student()
  y.setValue("Tom", 36, 11138)
  x.display()
  y.pr()

# %load ex06-06.py
class Person():
  def __init__(self, na, a):
    self.name = None
    self.age = None

  def birthYear(self):
    return 2019 - self.age

  def display(self):
    print("Name:", self.name, ", Age:", self.age)


class Teacher(Person):
  def __init__(self, na, a, sa):
    super().__init__(na, a)
    self.salary = sa

  def pr(self):
    super().display()
    print("Salary:", self.salary)


class Student(Person):
  def __init__(self, na, a, no):
    super().__init__(na, a)
    self.student_number = no

  def pr(self):
    super().display()
    print("StudNo:", self.student_number)


if __name__ == '__main__':
  x = Person("Alvin", 32)
  y = Student("Tom", 32, 11138)
  x.display()
  y.pr()

## 6.3 類別函數覆寫(override)

# %load ex06-07.py
class SalesPerson():
  def __init__(self, t):
    self.totalSales = t

  def bonus(self):
    return self.totalSales * 0.008


class SalesManager(SalesPerson):
  def __init__(self, t):
    super().__init__(t)

  def bonus(self):
    return self.totalSales * 0.008 + 1000


if __name__ == '__main__':
  Jim = SalesPerson(50000)
  print("Jim's Bonus:", Jim.bonus())
  Tom = SalesManager(45000)
  print("Tom's Bonus:", Tom.bonus())