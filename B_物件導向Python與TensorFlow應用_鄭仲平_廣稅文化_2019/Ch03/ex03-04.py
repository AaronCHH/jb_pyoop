class Rose():
  price = 0
  month = 0

  def __init__(self, p, m):
    self.price = p
    self.month = m

  def get_month(self):
    return self.month


if __name__ == '__main__':
  rose = Rose(8.28, 3)
  print("Month:", rose.get_month())
