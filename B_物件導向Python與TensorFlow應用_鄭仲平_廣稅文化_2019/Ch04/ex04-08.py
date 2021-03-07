class Money():
  def __init__(self, amt):
    self.balance = amt

  def add(self, saving):
    newObj = Money(self.balance + saving)
    return newObj
    # self.balance += saving
    # return self

  def display(self):
    print("Balance is:", self.balance)
    return self


if __name__ == '__main__':
  orange = Money(100)
  orange.display().add(300).display().add(80).display()
