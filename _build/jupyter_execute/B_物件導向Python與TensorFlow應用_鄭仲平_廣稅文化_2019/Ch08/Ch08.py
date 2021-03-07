# Ch08 多型 (Polymorphism)

## 8.2 多型 (Polymorphism)

# %load ex08-01.py
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


## 8.3 Function Overriding

# %load ex08-02.py
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
  p = []

  peter = SalesManager(5000)
  alvin = SalesEngineer(10000)
  lily = SalesEngineer(15000)

  p.append(peter)
  p.append(alvin)
  p.append(lily)

  for i in range(0, 3, 1):
    print(p[i].bonus())

# %load ex08-03.py
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

# %load ex08-04.py
from abc import ABC, abstractmethod


class Coin(ABC):
  @abstractmethod
  def onValue():
    pass


class one_dollar(Coin):
  def onValue(self):
    return 1.0


class five_dollar(Coin):
  def onValue(self):
    return 5.0


class ten_dollar(Coin):
  def onValue(self):
    return 10.0


class Wallet():
  def __init__(self):
    self.size = 0
    self.coll = []

  def feedCoin(self, c):
    self.coll.append(c)
    self.size += 1

  def value(self):
    return self.calculate_children_values()

  def calculate_children_values(self):
    self.mSum = 0

    for i in range(0, self.size, 1):
      self.mSum += self.coll[i].onValue()

    return self.mSum


class VendingMachine():
  def __init__(self):
    self.mWallet = Wallet()

  def feedCoin(self, c):
    self.mWallet.feedCoin(c)

  def showAmount(self):
    print("amt:", self.mWallet.value())


if __name__ == '__main__':
  vm = VendingMachine()
  coin = five_dollar()
  vm.feedCoin(coin)
  coin = ten_dollar()
  vm.feedCoin(coin)
  coin = one_dollar()
  vm.feedCoin(coin)
  vm.showAmount()

