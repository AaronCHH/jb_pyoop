class Container():
  child = None
  rSize = 0

  def setter(self, d_ref):
    self.child = d_ref
    self.rSize = self.child.getSize() * 2.5

  def getSize(self):
    return self.rSize


class Desk():
  dSize = 0

  def __init__(self):
    self.dSize = 12.5

  def getSize(self):
    return self.dSize


if __name__ == '__main__':
  aDesk = Desk()
  aContainer = Container()
  aContainer.setter(aDesk)
  print("Container.size", aContainer.getSize())