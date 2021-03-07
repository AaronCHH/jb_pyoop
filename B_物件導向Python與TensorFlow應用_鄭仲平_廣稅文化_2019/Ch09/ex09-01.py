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
