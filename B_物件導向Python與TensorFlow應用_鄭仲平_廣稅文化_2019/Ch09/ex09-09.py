from abc import ABC, abstractmethod


class UnderGraduate():
  def __init__(self, na):
    self.name = na

  def ComputeTuition(self, credit):
    if credit > 6:
      credit = 6

    return (credit - 1) * 500 + 5000


class Graduate():
  def __init__(self, na):
    self.name = na

  def ComputeTuition(self, credit):
    if credit > 6:
      credit = 6

    return credit * 700 + 5000


if __name__ == '__main__':
  Lily = UnderGraduate("Lily Wang")
  t1 = Lily.ComputeTuition(5)
  print("Lily:", t1)

  Peter = Graduate("Peter Sung")
  t2 = Peter.ComputeTuition(7)
  print("Peter:", t2)
