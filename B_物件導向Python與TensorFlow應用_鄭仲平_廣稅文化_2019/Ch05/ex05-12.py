class Employee():
  temp = 0

  def __init__(self, na, sa):
    self.emp_name = na
    self.salary = sa

  def save_to_temp(self):
    Employee.temp = self.salary

  def load_from_temp(self):
    self.salary = Employee.temp

  def Display(self):
    print("Name=", self.emp_name, ", Salary:", self.salary)


if __name__ == '__main__':
  tom = Employee("Tom", 7777.25)
  peter = Employee("Peter", 1643.5)

  tom.save_to_temp()
  peter.load_from_temp()

  peter.Display()