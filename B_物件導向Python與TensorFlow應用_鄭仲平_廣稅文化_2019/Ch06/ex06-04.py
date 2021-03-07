class Person():
  def setValue(self, na, a):
    self.name = na
    self.age = a

  def birthYear(self):
    return 2019 - self.age

  def display(self):
    print("Name:", self.name, ", Age:", self.age)


class Teacher(Person):
  def setValue(self, na, a, sa):
    super().setValue(na, a)
    self.salary = sa

  def pr(self):
    super().display()
    print("Salary:", self.salary)


class Student(Person):
  def setValue(self, na, a, no):
    super().setValue(na, a)
    self.student_number = no

  def pr(self):
    super().display()
    print("StudNo:", self.student_number)


if __name__ == '__main__':
  x = Person()
  x.setValue("Alvin", 32)
  y = Student()
  y.setValue("Tom", 36, 11138)
  x.display()
  y.pr()