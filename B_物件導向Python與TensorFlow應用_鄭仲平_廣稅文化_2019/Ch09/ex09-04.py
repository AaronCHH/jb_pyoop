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
