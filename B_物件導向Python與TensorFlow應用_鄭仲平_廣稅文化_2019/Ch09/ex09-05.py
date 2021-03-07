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
