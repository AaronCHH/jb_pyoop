from abc import ABC, abstractmethod


class SalesPerson(ABC):
  def __init__(self, na, sx):
    self.name = na
    self.sex = sx

  def SetFee(self, fee, disc):
    self.base_fee = fee
    self.discount = disc

  @abstractmethod
  def GetTotal(self):
    pass

  @abstractmethod
  def Display(self):
    pass


if __name__ == '__main__':
  alice = SalesPerson("Alice", "Male")
  alice.SetFee(2000, 0.8)
  alice.Display()
