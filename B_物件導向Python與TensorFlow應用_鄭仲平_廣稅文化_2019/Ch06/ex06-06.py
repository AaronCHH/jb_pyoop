class Person():
  def __init__(self, na, a):
    self.name = None
    self.age = None

  def birthYear(self):
    return 2019 - self.age

  def display(self):
    print("Name:", self.name, ", Age:", self.age)


class Teacher(Person):
  def __init__(self, na, a, sa):
    super().__init__(na, a)
    self.salary = sa

  def pr(self):
    super().display()
    print("Salary:", self.salary)


class Student(Person):
  def __init__(self, na, a, no):
    super().__init__(na, a)
    self.student_number = no

  def pr(self):
    super().display()
    print("StudNo:", self.student_number)


if __name__ == '__main__':
  x = Person("Alvin", 32)
  y = Student("Tom", 32, 11138)
  x.display()
  y.pr()