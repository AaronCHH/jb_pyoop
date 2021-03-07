class SalesPerson():
  def __init__(self, t):
    self.totalSales = t

  def bonus(self):
    return self.totalSales * 0.008


class SalesManager(SalesPerson):
  def __init__(self, t):
    super().__init__(t)

  def bonus(self):
    return self.totalSales * 0.008 + 1000


if __name__ == '__main__':
  Jim = SalesPerson(50000)
  print("Jim's Bonus:", Jim.bonus())
  Tom = SalesManager(45000)
  print("Tom's Bonus:", Tom.bonus())

