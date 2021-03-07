from abc import ABC, abstractmethod


class SalesPerson(ABC):
  def __init__(self, na, a):
    self.name = na
    self.total_amount = a

  def bonus(self):
    return self.total_amount * 0.008


class SalesEngineer(SalesPerson):
  def bonus(self):
    return super().bonus() + 500


class SalesManger(SalesPerson):
  def bonus(self):
    return super().bonus() + 1000


if __name__ == '__main__':
  z = SalesPerson("z's bonus:", 5000)
  print(z.name, z.bonus())

  y = SalesEngineer("y's bonus:", 10000)
  print(y.name, y.bonus())

  m = SalesEngineer("m's bonus:", 15000)
  print(m.name, m.bonus())
