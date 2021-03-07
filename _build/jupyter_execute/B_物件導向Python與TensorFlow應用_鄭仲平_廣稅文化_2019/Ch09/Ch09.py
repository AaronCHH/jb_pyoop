# Ch09 設計抽象類別

## 9.1 抽象

# %load ex09-01.py
from abc import ABC, abstractmethod


class Person():
  def SetName(self, na):
    self.name = na

  @abstractmethod
  def Display(self):
    pass


class Employee(Person):
  def SetName(self, na):
    super().SetName(na)

  def Display(self):
    print("Employee:", self.name)


if __name__ == '__main__':
  p = Employee()
  p.SetName("Peter Chen")
  p.Display()

## 9.2 抽象之步驟

# %load ex09-02.py
from abc import ABC, abstractmethod


class Customer():
  def SetName(self, na):
    self.name = na

  def Display(self):
    print("Cust:", self.name)


class Employee():
  def SetName(self, na):
    self.name = na

  def SetSalary(self, sa):
    self.salary = sa

  def Display(self):
    print("Emp:", self.name, ", SA:", self.salary)


if __name__ == '__main__':
  c = Customer()
  c.SetName("Tom Lin")
  c.Display()

  p = Employee()
  p.SetName("Peter Chen")
  p.SetSalary(50000)
  p.Display()

# %load ex09-03.py
from abc import ABC, abstractmethod


class Person():
  def SetName(self, na):
    self.name = na

  @abstractmethod
  def Display(self):
    pass


class Customer(Person):
  def Display(self):
    print("Cust:", self.name)


class Employee(Person):
  def SetSalary(self, sa):
    self.salary = sa

  def Display(self):
    print("Emp:", self.name, ", SA:", self.salary)


if __name__ == '__main__':
  c = Customer()
  c.SetName("Tom Lin")
  c.Display()

  p = Employee()
  p.SetName("Peter Chen")
  p.SetSalary(50000)
  p.Display()

# %load ex09-04.py
from abc import ABC, abstractmethod


class Person():
  coll = []
  counter = 0

  def __init__(self, na):
    self.name = na
    Person.coll.append(self)
    Person.counter += 1

  def Disp(self):
    for i in range(0, Person.counter, 1):
      self.coll[i].Display()

  @abstractmethod
  def Display(self):
    pass


class Customer(Person):
  def Display(self):
    print("Cust:", self.name)


class Employee(Person):
  def SetSalary(self, sa):
    self.salary = sa

  def Display(self):
    print("Emp:", self.name, ", SA:", self.salary)


if __name__ == '__main__':
  c = Customer("Tom Lin")
  p = Employee("Peter Chen")
  p.SetSalary(50000)
  c.Disp()
  print("=======================")
  p.Disp()

# %load ex09-05.py
from abc import ABC, abstractmethod


class Employee():
  def __init__(self, na, sex):
    self.name = na
    self.sex = sex

  def SetFee(self, fee, disc):
    self.base_fee = fee
    self.discount = disc

  def Display(self):
    mFee = self.base_fee * self.discount
    print(self.name, "'s fee:", mFee)


class Customer():
  def __init__(self, na, sex):
    self.name = na
    self.sex = sex

  def SetFee(self, fee, disc):
    self.ann_fee = fee
    self.discout = disc

  def Display(self):
    mAnnFee = self.ann_fee * self.discout
    print(self.name, "'s fee:", mAnnFee)


if __name__ == '__main__':
  emp = Employee("Tom", "M")
  cust = Customer("Lily", "F")
  emp.SetFee(1000, 0.9)
  cust.SetFee(500, 0.75)
  emp.Display()
  cust.Display()

# %load ex09-06.py
from abc import ABC, abstractmethod


class Person():
  def __init__(self, na, sex):
    self.name = na
    self.sex = sex


class Employee(Person):
  def SetFee(self, fee, disc):
    self.base_fee = fee
    self.discount = disc

  def Display(self):
    mFee = self.base_fee * self.discount
    print(self.name, "'s fee:", mFee)


class Customer(Person):
  def SetFee(self, fee, disc):
    self.ann_fee = fee
    self.discout = disc

  def Display(self):
    mFee = self.ann_fee * self.discout
    print(self.name, "'s fee:", mFee)


if __name__ == '__main__':
  emp = Employee("Tom", "M")
  cust = Customer("Lily", "F")
  emp.SetFee(1000, 0.9)
  cust.SetFee(500, 0.75)
  emp.Display()
  cust.Display()

# %load ex09-07.py
from abc import ABC, abstractmethod


class Person():
  def __init__(self, na, sex):
    self.name = na
    self.sex = sex


class Employee(Person):
  def SetFee(self, fee, disc):
    self.base_fee = fee
    self.discount = disc

  def Display(self):
    mFee = self.GetFee()
    print(self.name, "'s fee:", mFee)

  def GetFee(self):
    return self.base_fee * self.discount


class Customer(Person):
  def SetFee(self, fee, disc):
    self.ann_fee = fee
    self.discount = disc

  def Display(self):
    mFee = self.GetFee()
    print(self.name, "'s fee:", mFee)

  def GetFee(self):
    return self.ann_fee * self.discount


if __name__ == '__main__':
  emp = Employee("Tom", "M")
  cust = Customer("Lily", "F")
  emp.SetFee(1000, 0.9)
  cust.SetFee(500, 0.75)
  emp.Display()
  cust.Display()

# %load ex09-08.py
from abc import ABC, abstractmethod


class Person():
  def __init__(self, na, sex):
    self.name = na
    self.sex = sex

  def Display(self):
    mFee = self.GetFee()
    print(self.name, "'s fee:", mFee)

  @abstractmethod
  def GetFee(self):
    pass


class Employee(Person):
  def SetFee(self, fee, disc):
    self.base_fee = fee
    self.discount = disc

  def GetFee(self):
    return self.base_fee * self.discount


class Customer(Person):
  def SetFee(self, fee, disc):
    self.ann_fee = fee
    self.discount = disc

  def GetFee(self):
    return self.ann_fee * self.discount


if __name__ == '__main__':
  emp = Employee("Tom", "M")
  cust = Customer("Lily", "F")
  emp.SetFee(1000, 0.9)
  cust.SetFee(500, 0.75)
  emp.Display()
  cust.Display()

## 9.4 設計抽象類別

# %load ex09-09.py
from abc import ABC, abstractmethod


class UnderGraduate():
  def __init__(self, na):
    self.name = na

  def ComputeTuition(self, credit):
    if credit > 6:
      credit = 6

    return (credit - 1) * 500 + 5000


class Graduate():
  def __init__(self, na):
    self.name = na

  def ComputeTuition(self, credit):
    if credit > 6:
      credit = 6

    return credit * 700 + 5000


if __name__ == '__main__':
  Lily = UnderGraduate("Lily Wang")
  t1 = Lily.ComputeTuition(5)
  print("Lily:", t1)

  Peter = Graduate("Peter Sung")
  t2 = Peter.ComputeTuition(7)
  print("Peter:", t2)

# %load ex09-10.py
from abc import ABC, abstractmethod


class Tuition(ABC):
  @abstractmethod
  def GetValue(self, credit):
    pass


class UTuition(Tuition):
  def GetValue(self, credit):
    return (credit - 1) * 500


class GTuition(Tuition):
  def GetValue(self, credit):
    return credit * 700


class UnderGraduate():
  def __init__(self, na):
    self.name = na

  def Setter(self, tuiObj):
    self.tc = tuiObj

  def ComputeTuition(self, credit):
    if credit > 6:
      credit = 6

    return self.tc.GetValue(credit) + 5000


class Graduate():
  def __init__(self, na):
    self.name = na

  def Setter(self, tuiObj):
    self.tc = tuiObj

  def ComputeTuition(self, credit):
    if credit > 6:
      credit = 6

    return self.tc.GetValue(credit) + 5000


if __name__ == '__main__':
  Lily = UnderGraduate("Lily Wang")
  under_tui = UTuition()
  Lily.Setter(under_tui)
  t1 = Lily.ComputeTuition(5)
  print("Lily:", t1)

  Peter = Graduate("Peter Sung")
  grad_tui = GTuition()
  Peter.Setter(grad_tui)
  t2 = Peter.ComputeTuition(7)
  print("Peter:", t2)

# %load ex09-11.py
from abc import ABC, abstractmethod


class Tuition(ABC):
  @abstractmethod
  def GetValue(self, credit):
    pass


class UTuition(Tuition):
  def GetValue(self, credit):
    return (credit - 1) * 500


class GTuition(Tuition):
  def GetValue(self, credit):
    return credit * 700


class Student():
  def __init__(self, na):
    self.name = na

  def Setter(self, tuiObj):
    self.tc = tuiObj

  def ComputeTuition(self, credit):
    if credit > 6:
      credit = 6

    return self.tc.GetValue(credit) + 5000


if __name__ == '__main__':
  Lily = Student("Lily Wang")
  under_tui = UTuition()
  Lily.Setter(under_tui)
  t1 = Lily.ComputeTuition(5)
  print("Lily:", t1)

  Peter = Student("Peter Sung")
  grad_tui = GTuition()
  Peter.Setter(grad_tui)
  t2 = Peter.ComputeTuition(7)
  print("Peter:", t2)