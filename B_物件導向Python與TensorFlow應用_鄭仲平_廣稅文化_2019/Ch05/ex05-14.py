class Employee():
  counter = 0
  sum = 0

  @classmethod
  def NumberOfObject(cls):
    return cls.counter

  @classmethod
  def Average(cls):
    return cls.sum / cls.counter

  @classmethod
  def Display_Avg(cls):
    print("Average salary:", cls.Average())

  def __init__(self, na, sa):
    self.emp_name = na
    self.salary = sa
    Employee.counter += 1
    Employee.sum += self.salary

  def display(self):
    print("Number of Employee:", Employee.NumberOfObject())


if __name__ == '__main__':
  e1 = Employee("Tom", 25000.0)
  e2 = Employee("Lily", 20000.0)
  e1.display()
  Employee.Display_Avg()