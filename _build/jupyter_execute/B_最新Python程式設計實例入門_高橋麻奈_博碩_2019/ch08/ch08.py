# Ch08 類別

## 8.1 類別的基礎

## Sample1

class Person:

  def getName(self):
    return self.name

  def getAge(self):
    return self.age


pr = Person()
pr.name = "鈴木"
pr.age = 23

n = pr.getName()
a = pr.getAge()

print(n, "先生/小姐", a, "歲。")

## Sample2

class Person:

  def getName(self):
    return self.name

  def getAge(self):
    return self.age

pr1 = Person()
pr1.name = "鈴木"
pr1.age = 23
n1 = pr1.getName()
a1 = pr1.getAge()

pr2 = Person()
pr2.name = "佐藤"
pr2.age = 38
n2 = pr2.getName()
a2 = pr2.getAge()

print(n1, "先生/小姐", a1, "歲。")
print(n2, "先生/小姐", a2, "歲。")

## 8.2 建構子

## Sample3

class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def getName(self):
    return self.name

  def getAge(self):
    return self.age

pr = Person("鈴木", 23)

n = pr.getName()
a = pr.getAge()

print(n, "先生", a, "歲。")

# pr1 = Person()
# pr1.name = "鈴木"
# pr1.age = 23
# n1 = pr1.getName()
# a1 = pr1.getAge()

## 8.3 類別變數及類別方法

## Sample4

class Person:
  count = 0

  def __init__(self, name, age):
    Person.count = Person.count + 1

    self.name = name
    self.age = age

  def getName(self):
    return self.name

  def getAge(self):
    return self.age

  @classmethod
  def getCount(cls):
    return cls.count


pr1 = Person("鈴木", 23)
pr2 = Person("佐藤", 38)

pr1.name = "鈴木2"
pr1.age = 24

print(pr1.getName(), "先生/小姐", pr1.getAge(), "歲。")
print(pr2.getName(), "先生/小姐", pr2.getAge(), "歲。")
print("合計人數為", Person.getCount(), "人。")

class Person:
  count = 0

  def __init__(self, name, age):
    Person.count = Person.count + 1

    self.name = name
    self.__age = age

  def getName(self):
    return self.name

  def getAge(self):
    return self.__age

  @classmethod
  def getCount(cls):
    return cls.count


pr1 = Person("鈴木", 23)
pr2 = Person("佐藤", 38)

pr1.name = "鈴木2"
pr1.age = 24

print(pr1.getName(), "先生/小姐", pr1.getAge(), "歲。")
print(pr2.getName(), "先生/小姐", pr2.getAge(), "歲。")
print("合計人數為", Person.getCount(), "人。")

## 8.4 封裝

## 8.5 新的類別

# %load Sample5.py
class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def getName(self):
    return self.name

  def getAge(self):
    return self.age


class Customer(Person):
  def __init__(self, nm, ag, ad, tl):
    super().__init__(nm, ag)

    self.adr = ad
    self.tel = tl

  def getName(self):
    self.name = "客戶：" + self.name
    return self.name

  def getAdr(self):
    return self.adr

  def getTel(self):
    return self.tel


pr = Customer("鈴木", 23, "mmm@nnn.nn.jp", "xxx-xxx-xxxx")

nm = pr.getName()
ag = pr.getAge()
ad = pr.getAdr()
tl = pr.getTel()

print(nm, "先生/小姐", ag, "歲。")
print("E-mail：", ad, "電話號碼：", tl, "。")

## 8.6 與類別相關的主題

## 8.7 模組

# %load myclass.py
class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def getName(self):
    return self.name

  def getAge(self):
    return self.age


class Customer(Person):
  def __init__(self, nm, ag, ad, tl):
    super().__init__(nm, ag)

    self.adr = ad
    self.tel = tl

  def getName(self):
    self.name = "客戶" + self.name

    return self.name

  def getAdr(self):
    return self.adr

  def getTel(self):
    return self.tel

# %load Sample6.py
import myclass

pr = myclass.Customer("鈴木", 23, "mmm@nnn.nn.jp", "xxx-xxx-xxxx")

nm = pr.getName()
ag = pr.getAge()
ad = pr.getAdr()
tl = pr.getTel()

print(nm, "先生/小姐", ag, "歲。")
print("E-mail：", ad, "電話號碼：", tl, "。")

## 8.8 模組的應用

# %load Sample6.py
import myclass

pr = myclass.Customer("鈴木", 23, "mmm@nnn.nn.jp", "xxx-xxx-xxxx")

nm = pr.getName()
ag = pr.getAge()
ad = pr.getAdr()
tl = pr.getTel()

print(nm, "先生/小姐", ag, "歲。")
print("E-mail：", ad, "電話號碼：", tl, "。")

## 8.9 標準函式庫

# %load Sample7.py
import calendar

c = calendar.TextCalendar()
c.prmonth(2019, 10)

## References

* https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring

