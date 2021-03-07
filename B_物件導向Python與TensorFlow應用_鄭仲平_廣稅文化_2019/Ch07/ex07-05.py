from abc import ABC, abstractmethod


class SalesPerson(ABC):
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


class SalesEngineer(SalesPerson):
  def __init__(self, na, sx):
    super().__init__(na, sx)

  def Display(self):
    print("Name:", self.name)
    print("Fee:", self.GetTotal())


class SalesSecretary(SalesPerson):
  def __init__(self, na, sx):
    super().__init__(na, sx)

  def GetTotal(self):
    return super().GetTotal() - 100


if __name__ == '__main__':
  alice = SalesEngineer("Alice", "Male")
  alice.AddFee(2000)
  alice.Display()
  
  linda = SalesSecretary("Linda", "Female")
  linda.AddFee(5000)
  linda.Display()
