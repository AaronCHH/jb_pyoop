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


class Snoopy(IDance):
  def dance(self):
    print("Snoopy is dancing")

  def sing(self):
    print("Snoopy is singing")


class DancerFactory():
  def Create(self):
    return Snoopy()


if __name__ == '__main__':
  factor = DancerFactory()
  dancer = factor.Create()
  dancer.dance()
  dancer.sing()
