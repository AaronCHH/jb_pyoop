from abc import ABC, abstractmethod


class ICell(ABC):
  @abstractmethod
  def GetPower(self):
    pass

  @abstractmethod
  def SetLinkToNext(self, nc):
    pass


class ILight(ABC):
  @abstractmethod
  def AddCell(self, cp):
    pass

  @abstractmethod
  def Power(self):
    pass


class PanasonicCell(ICell):
  def __init__(self):
    self.pw = 10
    self.next_cell = None

  def SetLinkToNext(self, nc):
    self.next_cell = nc

  def GetPower(self):
    if self.next_cell == None:
      return self.pw
    else:
      return self.pw + self.next_cell.GetPower()


class CatCell(ICell):
  def __init__(self):
    self.pw = 5
    self.next_cell = None

  def SetLinkToNext(self, nc):
    self.next_cell = nc

  def GetPower(self):
    if self.next_cell == None:
      return self.pw
    else:
      return self.pw + self.next_cell.GetPower()


class FlashLight():
  def __init__(self):
    self.head = None
    self.tail = self.head

  def AddCell(self, cp):
    if self.head == None:
      self.head = cp
      self.tail = self.head
    else:
      self.tail.SetLinkToNext(cp)
      self.tail = cp

  def Power(self):
    return self.head.GetPower()


if __name__ == '__main__':
  light = FlashLight()
  cell = CatCell()
  light.AddCell(cell)
  print(light.Power())
  print("=======================")
  cell = PanasonicCell()
  light.AddCell(cell)
  cell = CatCell()
  light.AddCell(cell)
  print(light.Power())