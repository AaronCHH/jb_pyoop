class Container():
  child = None
  rSize = 0

  def setter(self, d_ref):
    self.child = d_ref
    self.rSize = 31.25
    self.child.setter(self)

  def getSize(self):
    return self.rSize


class Desk():
  parent = None
  dSize = 0

  def setter(self, c_ref):
    self.parent = c_ref
    self.dSize = self.parent.getSize() / 2.5

  def getSize(self):
    return self.dSize


if __name__ == '__main__':
  aDesk = Desk()
  aContainer = Container()
  aContainer.setter(aDesk)
  print("Desk.size", aDesk.getSize())
