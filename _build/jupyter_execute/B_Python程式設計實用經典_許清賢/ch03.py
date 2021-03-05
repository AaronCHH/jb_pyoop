# Ch03 類別結構及功能

## 3.1 類別結構與宣告

# %load person.py
#filename: person.py
# function: use _init_ to create the Attribute of object

class person:
  def __init__(self, name, age, edu, hobby):
    self.name = name
    self.age = age
    self.education = edu
    self.hobby = hobby


John_Pan = person('John', 35, "University", "Golf")
Lucy = person('Lucy', 32, "Master", "joggling")

print(John_Pan.name, John_Pan.age, John_Pan.education, John_Pan.hobby)
print(Lucy.name, Lucy.age, Lucy.education, Lucy.hobby)

# %load class_bank.py
# filename:class_bank.py (in chap3)
# function: using the class and _init_ and some method to process the bank operation
# _init_: the purpose of the self is that it refers to the specific object created from class like Account class

class Account:
  def __init__(self, acct_number, name):
    print("\t_init_ contstructor is processing")
    self.acct_number = acct_number
    self.name = name
    self.balance = 100

  def deposit(self, amount):
    print("Deposit amount is ", amount)
    if amount <= 0:
      raise ValueError('should be positive amount')
    self.balance += amount

  def withdraw(self, amount):
    print("Withdraw amount is ", amount)
    if amount <= self.balance:
      self.balance -= amount
    else:
      raise RuntimeError('Your account balance is not enough!!!')

# when you use your ATM card to withdraw momey,you must pass the password first
# the while loop is used to check the password


while True:
  print("\nPlease key in your Card password!!!")
  passwrd = input()
  if passwrd == "222222":
    acct1 = Account("0081038000111", 'Johnny Hsu')
    break
  else:
    continue
print("your current balance of card is:", acct1.balance)

print("\n start to prcocess the class object acct1")
deposit1 = acct1.deposit
withdraw1 = acct1.withdraw
acct1.deposit(2000)
deposit1(10000)
withdraw1(5000)
print("the bank balaance is ", acct1.balance)

print("\n start to prcocess the class object acct2")
acct2 = Account('00810380000222', 'Sean Pan ')
deposit2 = acct2.deposit
withdraw2 = acct2.withdraw
deposit2(3000)
withdraw2(2000)
print("the bank balance is ", acct2.balance)

## 3.2 資料及屬性

# %load class_attribute.py

class Class_attr:
  # class data is counter and class_fund
  counter = 0
  class_fund = 0

  def __init__(self):
    type(self).counter += 1

  def __del__(self):
    type(self).counter -= 1


if __name__ == "__main__":

  Tang = Class_attr()
  Class_attr.class_fund = Class_attr.counter*1000
  print("Number of instances: : ", Class_attr.counter)

  Big_David = Class_attr()
  Class_attr.class_fund = Class_attr.counter*1000
  print("Number of instances: : " + str(Class_attr.counter))

  del Big_David
  print("Number of instances: : " + str(Class_attr.counter))
  Class_attr.class_fund = Class_attr.counter*1000
  
  print(Class_attr.class_fund)

# %load employee.py
#filenme:Employee.py
#function : class variable and class attribute 

class Employee:
   """
   Class Doc show the class attribute
   """
#Count is class variable
   Count = 0

   def __init__(self, name, no, salary,level):
     
      self.name = name
      self.no = no
      self.salary = salary
      self.level = level
      Employee.Count += 1
   
   def displayEmployee(self):
      print("-"*45)
      print ("No : ", self.no,  ", Salary: ", self.salary,", Level: ", self.level)

#if __name__ == "__main__":
   
John= Employee("John", "126",52000,"Engineer")
Ted = Employee("Teddy","34", 65000,"Manager")
if hasattr(John, 'name') :
    John.displayEmployee()


setattr(Ted, 'salary', 68000)
Ted.displayEmployee()
print("Total Employee no is ",Employee.Count)


print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)


## 3.3 類別方法

# %load stacking.py
# filename:stacking.py
# funcion: define _init_ using the empty list first
# push the items in the stack ... and so on

class Stack:
  def __init__(self):
    print("_init_ is doing")
    self.items = []

  # method push purpose is to push items
  def push(self, item):
    self.items.append(item)

  # method pop
  def pop(self):
    if len(self.items) == 0:
      raise ValueError('should have data in stack first')
    else:
      return self.items.pop()

  # isempty method is to check if stack is empty
  def isempty(self):
    return (self.items == [])

  # method to check how many items in the stack
  def countofstack(self):
    return len(self.items)

  def __str__(self):
    return str(self.items)


if __name__ == "__main__":

  stackobj = Stack()
 # print( stackobj)
 # stackobj.pop()

  stackobj.push("Johnny")
  stackobj.push("score")
  print(stackobj)

  stackobj.pop()
  print(stackobj)

  print("the items count of stack is", stackobj.countofstack())

# %load llist_text.py

# filename:llist_text.py
# function: build linked list

class Node:
  def __init__(self, data):
    print("init node")
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    print("Init List")
    self.head = None
    self.tail = None

  def Add(self, data):
    print("Node data=", data)
    newnode = Node(data)

    if self.head == None:
      self.head = newnode
    if self.tail != None:
      self.tail.next = newnode

    self.tail = newnode

  def PrintList(self):
    node = self.head
    while node != None:
      print(node.data)
      node = node.next


LList = LinkedList()
LList.Add("John")
LList.Add("Johnny")
LList.Add("CT")
print("The linked list is ")
LList.PrintList()

# %load staticmethod.py
# filename:staticmethod.py
# funcion:specail methods of Python

# @staticmethod means: when this method is called,
# indeed, no need to pass an instance of the class to it , we(as we normally do with methods).
# This means you can put a function inside a class
# No need to have a instance .but you can't access the instance of that class (this is useful when your method does not use the instance).
# We no need to have a instance, we can use classname.Methodname() to access
# @classmethod means: when this method is called
# use class as the first argument instead of instance of that class (as we normally do with methods).
# This means you can use the class and its properties inside that method rather than a particular instance.

# @staticmethod: no need the slef and the class cls parameter , use it like the function way。
# @classmethod: noe need the self parameter, but the first parameter need to use cls, which means the cls parameter。


class StaticClass(object):
  count = 0

  def forking(self):
    print('forking')

  @staticmethod
  def static_way():
    print('static_way')
    print(StaticClass.count)
    StaticClass.count += 1
# cls().forking()
# NameError: name 'cls' is not defined

  @classmethod
  def class_way(cls):
    print('class_way')
    print(cls.count)
    cls.count += 1
    cls().forking()


StaticClass.class_way()
StaticClass.static_way()
StaticClass.class_way()

## 3.4 建構(初始)函式

# %load class_linuxsignal.py
# filename:class_linuxsignal
# function: test the _init_
class Linuxsignal:
  process_counter = 0

  def __init__(self):
    print("Class object is inited now")
    type(self).process_counter += 1

  def linuxInstances(self):
    return Linuxsignal.process_counter


if __name__ == "__main__":

  x = Linuxsignal()
  print(x.linuxInstances())
  y = Linuxsignal()
  print(x.linuxInstances())

# %load exam3-2.py
#filename:Animalstore.py
#function: Class has Name and list

class Animal_Store:

#class has Name and list attribute
    def __init__(self, name):
        self.name = name
        self.list = []    

    def add_description(self, nick):
        self.list.append(nick)

Wu = Animal_Store('Amira')
Tsai = Animal_Store('Panda')

Wu.add_description('He can play ball')
Wu.add_description('and can smile to child')
Tsai.add_description('He can dance')

print(Wu.list)
print(Tsai.list)



# %load exam3-3.py
#filenme:exam3-3-Employee.py
#function : class variable and class attribute 

class Employee:
   """
   Class Doc show the class attribute
   """
#Count is class variable
   Count = 0

   def __init__(self, name, no, salary,level):
     
      self.name = name
      self.no = no
      self.salary = salary
      self.level = level
      Employee.Count += 1
   
   def displayEmployee(self):
      print("-"*45)
      print ("No : ", self.no,  ", Salary: ", self.salary,", Level: ", self.level)

print ( Employee.__module__)
#if __name__ == "__main__":
   
John= Employee("John", "126",52000,"Engineer")
Ted = Employee("Teddy","34", 65000,"Manager")

print("Object ID ",id(John),"  ",id(Ted))
del Ted
print("Object ID ",id(John),"  ",id(Ted))
