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