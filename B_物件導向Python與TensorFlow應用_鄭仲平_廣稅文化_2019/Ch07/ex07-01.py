class SalesPerson():
  def __init__(self, na, sx):
    self.name = na
    self.sex = sx

  def SetFee(self, fee, disc):
    self.base_fee = fee
    self.discount = disc

  def GetTotal(self):
    return self.base_fee * self.discount

  def Display(self):
    print("Name:", self.name)
    print("Fee:", self.GetTotal())


if __name__ == '__main__':
  alice = SalesPerson("Alice", "Male")
  alice.SetFee(2000, 0.8)
  alice.Display()
