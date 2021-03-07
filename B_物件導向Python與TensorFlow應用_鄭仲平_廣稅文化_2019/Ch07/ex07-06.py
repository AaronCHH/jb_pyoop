from abc import ABC, abstractmethod


class SalesPerson(ABC):
  def __init__(self, na, sx):
    self.name = na
    self.sex = sx

  def SetFee(self, fee, disc):
    self.base_fee = fee
    self.discount = disc

  def display(self):
    print("Fee:", self.GetTotal())

  @abstractmethod
  def GetTotal(self):
    pass


class SalesSecretary(SalesPerson):
  def __init__(self, na, sx):
    super().__init__(na, sx)

  def GetTotal(self):
    return self.base_fee * self.discount - 100


if __name__ == '__main__':
  linda = SalesSecretary("Linda", "Female")
  linda.SetFee(5000, 0.7)
  linda.display()
