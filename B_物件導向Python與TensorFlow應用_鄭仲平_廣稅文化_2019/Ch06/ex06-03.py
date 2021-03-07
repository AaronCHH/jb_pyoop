class Person():
  def setValue(self, na, a):
    self.name = na
    self.age = a

  def birthYear(self):
    return 2019 - self.age

  def display(self):
    print("Name:", self.name, ", Age:", self.age)


class Teacher(Person):
  def tr_setValue(self, na, a, sa):
    super().setValue(na, a)
    self.salary = sa

  def pr(self):
    super().display()
    print("Salary:", self.salary)


if __name__ == '__main__':
  steven = Teacher()
  steven.tr_setValue("Steven", 35, 35000)
  steven.pr()
