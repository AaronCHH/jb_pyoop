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
