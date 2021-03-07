class Rose():
  price = 0
  month = 0

  def __init__(self, p, m):
    self.price = p
    self.month = m

  def get_month(self):
    return self.month


if __name__ == '__main__':

  def display(x):
    print("Month:", x.get_month())

  r1 = Rose(10.25, 10)
  r2 = Rose(8.5, 6)

  display(r1)
  display(r2)
