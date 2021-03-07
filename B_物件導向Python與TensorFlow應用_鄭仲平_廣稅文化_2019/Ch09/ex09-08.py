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
