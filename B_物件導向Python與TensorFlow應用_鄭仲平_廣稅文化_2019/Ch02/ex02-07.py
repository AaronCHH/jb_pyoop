# Ex02-01
class Tree():
  def __init__(self, v, a, h):
    self.variety = v
    self.age = a
    self.height = h


class FruitTree(Tree):
  def __init__(self, v, a, h, m, p):
    self.variety = v
    self.age = a
    self.height = h
    self.month = m
    self.price = p

  def computeAmount(self, weight):
    return weight * self.price

  def inquireHeight(self):
    return self.height

  def SetHeight(self, h):
    self.height = h

  def SetPrice(self, p):
    self.price = p


class Bamboo(Tree):
  def __init__(self, v, a, h, u):
    self.variety = v
    self.age = a
    self.height = h
    self.usage = u


if __name__ == '__main__':
  a = FruitTree("peach", 8, 2.1, 3, 20)

  a.SetPrice(30)
  a.SetHeight(2.6)

  amount = a.computeAmount(25)
  height = a.inquireHeight()
  print(amount, height)
