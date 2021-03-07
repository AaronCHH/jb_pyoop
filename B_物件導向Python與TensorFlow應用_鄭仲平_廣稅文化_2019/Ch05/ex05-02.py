class Tree():
  def input(self, hei):
    self.variety = None
    self.age = None
    self.height = hei


if __name__ == '__main__':
  a = Tree()
  a.input(2.1)
  print("Set a.height to  ", a.height)