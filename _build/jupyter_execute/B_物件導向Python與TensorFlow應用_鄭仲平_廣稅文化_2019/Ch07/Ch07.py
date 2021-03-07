# Ch07 抽象類別 (abstract class)

## 7.2 abstract class

# %load ex07-01.py
class SalesPerson():
  def __init__(self, na, sx):
    self.name = na
    self.sex = sx

  def SetFee(self, fee, disc):
    self.base_fee = fee
    self.discount = disc

  def GetTotal(self):
    return self.base_fee * self.discount

  def Display(self):
    print("Name:", self.name)
    print("Fee:", self.GetTotal())


if __name__ == '__main__':
  alice = SalesPerson("Alice", "Male")
  alice.SetFee(2000, 0.8)
  alice.Display()


# %load ex07-02.py
from abc import ABC, abstractmethod


class SalesPerson(ABC):
  def __init__(self, na, sx):
    self.name = na
    self.sex = sx

  def SetFee(self, fee, disc):
    self.base_fee = fee
    self.discount = disc

  @abstractmethod
  def GetTotal(self):
    pass

  @abstractmethod
  def Display(self):
    pass


if __name__ == '__main__':
  alice = SalesPerson("Alice", "Male")
  alice.SetFee(2000, 0.8)
  alice.Display()


## 7.3 實作抽象類別

# %load ex07-03.py
from abc import ABC, abstractmethod


class SalesPerson(ABC):
  def __init__(self, na, sx):
    self.name = na
    self.sex = sx

  def SetFee(self, fee, disc):
    self.base_fee = fee
    self.discount = disc

  @abstractmethod
  def GetTotal(self):
    pass

  @abstractmethod
  def Display(self):
    pass


class SalesEngineer(SalesPerson):
  def __init__(self, na, sx):
    super().__init__(na, sx)

  def GetTotal(self):
    return self.base_fee * self.discount

  def Display(self):
    print("Name:", self.name)
    print("Fee:", self.GetTotal())


if __name__ == '__main__':
  alice = SalesEngineer("Alice", "Male")
  alice.SetFee(2000, 0.8)
  alice.Display()


# %load ex07-04.py
from abc import ABC, abstractmethod


class SalesPerson(ABC):
  @abstractmethod
  def AddFee(self, fee):
    pass

  @abstractmethod
  def GetTotal(self):
    pass

  @abstractmethod
  def Display(self):
    pass


class SalesEngineer(SalesPerson):
  def __init__(self, na, sx):
    self.name = na
    self.sex = sx
    self.base_fee = 1000
    self.discount = 0.5

  def AddFee(self, fee):
    self.base_fee += fee

  def GetTotal(self):
    return self.base_fee * self.discount

  def Display(self):
    print("Name:", self.name)
    print("Fee:", self.GetTotal())


if __name__ == '__main__':
  alice = SalesEngineer("Alice", "Male")
  alice.AddFee(2000)
  alice.Display()


## 7.4 抽象類別之預設行為

# %load ex07-05.py
from abc import ABC, abstractmethod


class SalesPerson(ABC):
  def __init__(self, na, sx):
    self.name = na
    self.sex = sx
    self.base_fee = 1000
    self.discount = 0.5
    
  # Default function
  def AddFee(self, fee):
    self.base_fee += fee

  def GetTotal(self):
    return self.base_fee * self.discount

  def Display(self):
    print("Name:", self.name)
    print("Fee:", self.GetTotal())


class SalesEngineer(SalesPerson):
  def __init__(self, na, sx):
    super().__init__(na, sx)

  def Display(self):
    print("Name:", self.name)
    print("Fee:", self.GetTotal())


class SalesSecretary(SalesPerson):
  def __init__(self, na, sx):
    super().__init__(na, sx)

  def GetTotal(self):
    return super().GetTotal() - 100


if __name__ == '__main__':
  alice = SalesEngineer("Alice", "Male")
  alice.AddFee(2000)
  alice.Display()
  
  linda = SalesSecretary("Linda", "Female")
  linda.AddFee(5000)
  linda.Display()


## 7.5 預設函數之反向呼叫

# %load ex07-06.py
from abc import ABC, abstractmethod


class SalesPerson(ABC):
  def __init__(self, na, sx):
    self.name = na
    self.sex = sx

  def SetFee(self, fee, disc):
    self.base_fee = fee
    self.discount = disc

  def display(self):
    print("Fee:", self.GetTotal())

  @abstractmethod
  def GetTotal(self):
    pass


class SalesSecretary(SalesPerson):
  def __init__(self, na, sx):
    super().__init__(na, sx)

  def GetTotal(self):
    return self.base_fee * self.discount - 100


if __name__ == '__main__':
  linda = SalesSecretary("Linda", "Female")
  linda.SetFee(5000, 0.7)
  linda.display()  # 反向呼叫

# %load ex07-07.py
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
