class Tree():
  def input(self, v, a, hei):
    self.__variety = v
    self.__age = a
    self.__height = hei

  def Show(self):
    print(self.__variety, self.__age, self.__height)


if __name__ == '__main__':
  a = Tree()
  b = Tree()
  a.input("peach", 8, 2.1)
  b.input("pineapple", 2, 0.5)

  a.Show()
  b.Show()
