class Money():
  def __init__(self, amt):
    self.balance = amt

  def add(self, saving):
    self.balance += saving

  def display(self):
    print("Balance is:", self.balance)


if __name__ == '__main__':
  orange = Money(100)
  orange.add(300)
  orange.add(80)
  orange.display()
