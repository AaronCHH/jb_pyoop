class Person():
  def setValue(self, na, a):
    self.name = na
    self.age = a

  def birthYear(self):
    return 2019 - self.age

  def display(self):
    print("Name:", self.name, ", Age:", self.age)


if __name__ == '__main__':
  mike = Person()
  mike.setValue("Mike", 45)
  mike.display()
  print("BirthYear:", mike.birthYear())
