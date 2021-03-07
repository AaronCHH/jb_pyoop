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


class SalesEngineer(SalesPerson):
  def __init__(self, na, sx):
    super().__init__(na, sx)

  def GetTotal(self):
    return self.base_fee * self.discount

  def Display(self):
    print("Name:", self.name)
    print("Fee:", self.GetTotal())


if __name__ == '__main__':
  alice = SalesEngineer("Alice", "Male")
  alice.SetFee(2000, 0.8)
  alice.Display()
