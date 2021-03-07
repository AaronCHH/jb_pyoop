from abc import ABC, abstractmethod


class IDance(ABC):
  @abstractmethod
  def dance(self):
    pass

  @abstractmethod
  def sing(self):
    pass


class Bear(IDance):
  def dance(self):
    print("Bear is dancing")

  def sing(self):
    print("Bear is singing")


class Dog(IDance):
  def dance(self):
    print("Dog is dancing")

  def sing(self):
    print("Dog is singing")


class DancerFactory():
  def Create(self):
    return Dog()

if __name__ == '__main__':
  factor = DancerFactory()        
  dancer = factor.Create()
  dancer.dance()
  dancer.sing()
