class Tree():
  def input(self, hei):
    self.__variety = None
    self.__height = 2.1
    self.age = None

  def ShowAge(self):
    print("Age = ", self.age)


if __name__ == '__main__':
  a = Tree()
  a.age = 8
  a.age += 2
  a.ShowAge()
