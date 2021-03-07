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


class Bamboo(Tree):
  def __init__(self, v, a, h, u):
    self.variety = v
    self.age = a
    self.height = h
    self.usage = u


if __name__ == '__main__':
  x = FruitTree("peach", 8, 2.1, 3, 20)
  print(x.variety, x.height, x.month, x.price)

  a = Bamboo("green", 2, 10.0, "chopstick")
  print(a.variety, a.age, a.height, a.usage)
