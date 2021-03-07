class Person():
  def setValue(self, na, a):
    self.name = na
    self.age = a

  def birthYear(self):
    return 2019 - self.age

  def display(self):
    print("Name:", self.name, ", Age:", self.age)


class Teacher(Person):
  pass


if __name__ == '__main__':
  steven = Teacher()
  steven.setValue("Steven", 45)
  steven.display()
