from abc import ABC, abstractmethod


class IPower(ABC):
  @abstractmethod
  def GetPower(self):
    pass


class PanasonicCell(IPower):
  def __init__(self):
    self.pw = 2

  def GetPower(self):
    return self.pw


class CatCell(IPower):
  def __init__(self):
    self.pw = 3

  def GetPower(self):
    return self.pw


class FlashLight():
  def __init__(self):
    self.cell_list = []
    self.index = 0

  def AddCell(self, cp):
    self.cell_list.append(cp)
    self.index += 1

  def Power(self):
    mSum = 0
    for i in range(0, self.index, 1):
      mSum += self.cell_list[i].GetPower()
    return mSum


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