class Person():
  def __init__(self, na, a):
    self.name = na
    self.age = a

  def birth_year(self):
    return 2019 - self.age

  def display(self):
    print("Name:", self.name, "B.Year:", self.birth_year())


class Teacher(Person):
  def __init__(self, na, a, s):
    super().__init__(na, a)
    self.salary = s

  def display(self):
    super().display()
    print("Salary:", self.salary)


if __name__ == '__main__':
  tr = Teacher("Steven:", 20, 35000)
  tr.display()
