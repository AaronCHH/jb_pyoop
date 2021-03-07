class Employee():
  counter = 0
  sum = 0

  def __init__(self, na, sa):
    self.emp_name = na
    self.salary = sa
    Employee.counter += 1
    Employee.sum += self.salary

  def Display_Avg(self):
    print("The number of employee:", Employee.counter)
    print("Average salary:", Employee.sum / Employee.counter)

  def Display(self):
    print("Name=", self.emp_name, ", Salary:", self.salary)


if __name__ == '__main__':
  e1 = Employee("Tom", 25000.0)
  e2 = Employee("Lily", 20000.0)
  e1.Display()
  e2.Display()
  e1.Display_Avg()