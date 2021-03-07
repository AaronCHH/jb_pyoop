from abc import ABC, abstractmethod


class SalesPerson(ABC):
  @abstractmethod
  def AddFee(self, fee):
    pass

  @abstractmethod
  def GetTotal(self):
    pass

  @abstractmethod
  def Display(self):
    pass


class SalesEngineer(SalesPerson):
  def __init__(self, na, sx):
    self.name = na
    self.sex = sx
    self.base_fee = 1000
    self.discount = 0.5

  def AddFee(self, fee):
    self.base_fee += fee

  def GetTotal(self):
    return self.base_fee * self.discount

  def Display(self):
    print("Name:", self.name)
    print("Fee:", self.GetTotal())


if __name__ == '__main__':
  alice = SalesEngineer("Alice", "Male")
  alice.AddFee(2000)
  alice.Display()
