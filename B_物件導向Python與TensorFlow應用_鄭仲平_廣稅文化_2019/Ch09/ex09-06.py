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
