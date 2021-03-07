class Tree():
  def input(self, hei):
    self.variety = None
    self.age = None
    self.height = hei

  def input(self, hei):
    self.height = hei

  def inquireHeight(self):
    return self.height


if __name__ == '__main__':
  a = Tree()
  a.input(2.1)
  h = a.inquireHeight()
  print("height = ", h, "公尺")