from abc import ABC, abstractmethod


class Tuition(ABC):
  @abstractmethod
  def GetValue(self, credit):
    pass


class UTuition(Tuition):
  def GetValue(self, credit):
    return (credit - 1) * 500


class GTuition(Tuition):
  def GetValue(self, credit):
    return credit * 700


class UnderGraduate():
  def __init__(self, na):
    self.name = na

  def Setter(self, tuiObj):
    self.tc = tuiObj

  def ComputeTuition(self, credit):
    if credit > 6:
      credit = 6

    return self.tc.GetValue(credit) + 5000


class Graduate():
  def __init__(self, na):
    self.name = na

  def Setter(self, tuiObj):
    self.tc = tuiObj

  def ComputeTuition(self, credit):
    if credit > 6:
      credit = 6

    return self.tc.GetValue(credit) + 5000


if __name__ == '__main__':
  Lily = UnderGraduate("Lily Wang")
  under_tui = UTuition()
  Lily.Setter(under_tui)
  t1 = Lily.ComputeTuition(5)
  print("Lily:", t1)

  Peter = Graduate("Peter Sung")
  grad_tui = GTuition()
  Peter.Setter(grad_tui)
  t2 = Peter.ComputeTuition(7)
  print("Peter:", t2)
