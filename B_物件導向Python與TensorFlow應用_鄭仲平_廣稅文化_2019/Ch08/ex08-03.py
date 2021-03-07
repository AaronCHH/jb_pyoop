from abc import ABC, abstractmethod


class SalesPerson(ABC):
  def __init__(self, a):
    self.total_amount = a

  def bonus(self):
    return self.total_amount * 0.008


class SalesEngineer(SalesPerson):
  def bonus(self):
    return super().bonus() + 500


class SalesManager(SalesPerson):
  def bonus(self):
    return super().bonus() + 1000


if __name__ == '__main__':

  def comp_bonus(sp):
    print(sp.bonus())

  p = []

  peter = SalesManager(5000)
  alvin = SalesEngineer(10000)
  lily = SalesEngineer(15000)

  p.append(peter)
  p.append(alvin)
  p.append(lily)

  for i in range(0, 3, 1):
    comp_bonus(p[i])
