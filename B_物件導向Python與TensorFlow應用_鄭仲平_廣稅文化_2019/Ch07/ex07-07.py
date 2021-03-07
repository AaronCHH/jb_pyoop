from abc import ABC, abstractmethod


class Person(ABC):
  def __init__(self, na):
    self.name = na

  @abstractmethod
  def display(self):
    pass


class Customer(Person):
  def display(self):
    print("Customer:", self.name)


class Product():
  def __init__(self, no):
    self.pno = no

  def soldTo(self, cobj):
    self.pc = cobj

  def inquire(self):
    self.disp()
    print("sold to ...")
    self.pc.display()

  @abstractmethod
  def disp(self):
    pass


class VIP(Customer):
  def __init__(self, na, t):
    super().__init__(na)
    self.tel = t

  def display(self):
    super().display()
    print("TEL:", self.tel)


class TV(Product):
  def __init__(self, no, pr):
    super().__init__(no)
    self.price = pr

  def disp(self):
    print("TV No:", self.pno)
    print("Price:", self.price)


if __name__ == '__main__':
  t = TV(1100, 1800.5)
  vp = VIP("Peter", "666-8899")
  t.soldTo(vp)
  t.inquire()
