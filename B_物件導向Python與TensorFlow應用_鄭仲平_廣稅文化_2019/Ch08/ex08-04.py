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
