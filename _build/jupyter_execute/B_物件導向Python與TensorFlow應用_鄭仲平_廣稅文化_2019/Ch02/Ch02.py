# Ch02 物件與類別

## 2.4 AKO 抽象關係

# %load ex02-01.py
# Ex02-01
class Tree():
  def __init__(self, v, a, h):
    self.variety = v
    self.age = a
    self.height = h


if __name__ == '__main__':
  x = Tree("Rose", 2, 3.5)
  print(x.variety, x.age, x.height)

# %load ex02-03.py
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

## 2.5 物件行為與介面

# %load ex02-06.py
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


class Bamboo(Tree):
  def __init__(self, v, a, h, u):
    self.variety = v
    self.age = a
    self.height = h
    self.usage = u


if __name__ == '__main__':
  a = FruitTree("peach", 8, 2.1, 3, 20)
  k = FruitTree("Apple", 5, 0.5, 7, 10)

  amount = a.computeAmount(25)
  height = a.inquireHeight()
  print(amount, height)

  amount = k.computeAmount(25)
  height = k.inquireHeight()
  print(amount, height)

# %load ex02-07.py
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