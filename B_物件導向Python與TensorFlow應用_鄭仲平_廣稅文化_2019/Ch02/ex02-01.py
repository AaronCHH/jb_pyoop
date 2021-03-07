# Ex02-01
class Tree():
  def __init__(self, v, a, h):
    self.variety = v
    self.age = a
    self.height = h


if __name__ == '__main__':
  x = Tree("Rose", 2, 3.5)
  print(x.variety, x.age, x.height)
