# Ch10 介面 (Interface)

## 10.2 以抽象類別實現界面

# %load ex10-01.py
from abc import ABC, abstractmethod


class IDance(ABC):
  @abstractmethod
  def dance(self):
    pass

  @abstractmethod
  def sing(self):
    pass


class Bear(IDance):
  def dance(self):
    print("Bear is dancing")

  def sing(self):
    print("Bear is singing")


class Dog(IDance):
  def dance(self):
    print("Dog is dancing")

  def sing(self):
    print("Dog is singing")


class DancerFactory():
  def Create(self):
    return Dog()


if __name__ == '__main__':
  factor = DancerFactory()
  dancer = factor.Create()
  dancer.dance()
  dancer.sing()

# %load ex10-02.py
from abc import ABC, abstractmethod


class IDance(ABC):
  @abstractmethod
  def dance(self):
    pass

  @abstractmethod
  def sing(self):
    pass


class Bear(IDance):
  def dance(self):
    print("Bear is dancing")

  def sing(self):
    print("Bear is singing")


class Snoopy(IDance):
  def dance(self):
    print("Snoopy is dancing")

  def sing(self):
    print("Snoopy is singing")


class DancerFactory():
  def Create(self):
    return Snoopy()


if __name__ == '__main__':
  factor = DancerFactory()
  dancer = factor.Create()
  dancer.dance()
  dancer.sing()

## 10.3 並聯電池物件

# %load ex10-03.py
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

## 10.4 串連電池物件

# %load ex10-04.py
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

## 10.5 Chain Of Responsibility 設計模式

# %load ex10-05.py
from abc import ABC, abstractmethod


class IHandle(ABC):
  @abstractmethod
  def HandleRequest(self, request):
    pass

  @abstractmethod
  def SetSuccessor(self, nc):
    pass


class ILight(ABC):
  @abstractmethod
  def AddCell(self, cp):
    pass

  @abstractmethod
  def Power(self, message):
    pass


class Handle(IHandle):
  def __init__(self):
    self.successor = None
    self.pw = 0

  def HandleRequest(self, request):
    if self.RequestForMe(request) == True:
      if self.successor == None:
        return self.pw
      else:
        return self.pw + self.successor.HandleRequest(request)
    else:
      if self.successor == None:
        return 0
      else:
        return self.successor.HandleRequest(request)

  @abstractmethod
  def RequestForMe(self, request):
    pass

  def SetSuccessor(self, nc):
    self.successor = nc


class PanasonicCell(Handle):
  def __init__(self):
    super().__init__()
    self.pw = 10

  def RequestForMe(self, msg):
    if msg == "Pan" or msg == "All":
      return True
    else:
      return False


class CatCell(Handle):
  def __init__(self):
    super().__init__()
    self.pw = 7

  def RequestForMe(self, msg):
    if msg == "Cat" or msg == "All":
      return True
    else:
      return False


class FlashLight():
  def __init__(self):
    self.head = None
    self.tail = self.head

  def AddCell(self, cp):
    if self.head == None:
      self.head = cp
      self.tail = self.head
    else:
      self.tail.SetSuccessor(cp)
      self.tail = cp

  def Power(self, message):
    if self.head == None:
      return 0
    else:
      return self.head.HandleRequest(message)


if __name__ == '__main__':
  light = FlashLight()
  pp = PanasonicCell()
  light.AddCell(pp)
  cc = CatCell()
  light.AddCell(cc)

  cc2 = CatCell()
  light.AddCell(cc2)
  pp = PanasonicCell()

  light.AddCell(pp)

  print(light.Power("All"))
  print("=======================")
  print(light.Power("Cat"))
  print("=======================")
  print(light.Power("Pan"))