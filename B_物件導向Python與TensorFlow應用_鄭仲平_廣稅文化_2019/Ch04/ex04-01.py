class Fee():
  def __init__(self, amt):
    self.amount = amt

  def disp(self):
    print("Amount is:", self.amount)


if __name__ == '__main__':
  a = Fee(100)
  b = Fee(80)
  a.disp()
  b.disp()
