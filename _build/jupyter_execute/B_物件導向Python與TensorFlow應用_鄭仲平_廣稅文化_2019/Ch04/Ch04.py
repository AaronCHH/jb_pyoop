# Ch04 物件之組合

## 4.1 self

# %load ex04-01.py
class Fee():
  def __init__(self, amt):
    self.amount = amt

  def disp(self):
    print("Amount is:", self.amount)


if __name__ == '__main__':
  a = Fee(100)
  b = Fee(80)
  a.disp()
  b.disp()

## 4.2 物件之包含關係

# %load ex04-02.py
class Container():
  child = None
  rSize = 0

  def setter(self, d_ref):
    self.child = d_ref
    self.rSize = self.child.getSize() * 2.5

  def getSize(self):
    return self.rSize


class Desk():
  dSize = 0

  def __init__(self):
    self.dSize = 12.5

  def getSize(self):
    return self.dSize


if __name__ == '__main__':
  aDesk = Desk()
  aContainer = Container()
  aContainer.setter(aDesk)
  print("Container.size", aContainer.getSize())

# %load ex04-03.py
class Container():
  child = None
  rSize = 0

  def setter(self, d_ref):
    self.child = d_ref
    self.rSize = 31.25
    self.child.setter(self)

  def getSize(self):
    return self.rSize


class Desk():
  parent = None
  dSize = 0

  def setter(self, c_ref):
    self.parent = c_ref
    self.dSize = self.parent.getSize() / 2.5

  def getSize(self):
    return self.dSize


if __name__ == '__main__':
  aDesk = Desk()
  aContainer = Container()
  aContainer.setter(aDesk)
  print("Desk.size", aDesk.getSize())

## 4.3 self(2)

# %load ex04-04.py
class Money():
  def __init__(self, amt):
    self.balance = amt

  def add(self, saving):
    self.balance += saving

  def display(self):
    print("Balance is:", self.balance)


if __name__ == '__main__':
  orange = Money(100)
  orange.add(300)
  orange.add(80)
  orange.display()

# %load ex04-05.py
class Money():
  def __init__(self, amt):
    self.balance = amt

  def add(self, saving):
    self.balance += saving
    return self

  def display(self):
    print("Balance is:", self.balance)


if __name__ == '__main__':
  orange = Money(100)
  orange.add(300).add(80)
  orange.display()

# %load ex04-06.py
class Money():
  def __init__(self, amt):
    self.balance = amt

  def add(self, saving):
    self.balance += saving
    return self

  def display(self):
    print("Balance is:", self.balance)


if __name__ == '__main__':
  orange = Money(100)
  orange.add(300).add(80).display()

## self

# %load ex04-07.py
class Money():
  def __init__(self, amt):
    self.balance = amt

  def add(self, saving):
    newObj = Money(self.balance + saving)
    return newObj
    # self.balance += saving
    # return self

  def display(self):
    print("Balance is:", self.balance)


if __name__ == '__main__':
  orange = Money(100)
  orange.add(300).add(80).display()

# %load ex04-08.py
class Money():
  def __init__(self, amt):
    self.balance = amt

  def add(self, saving):
    newObj = Money(self.balance + saving)
    return newObj
    # self.balance += saving
    # return self

  def display(self):
    print("Balance is:", self.balance)
    return self


if __name__ == '__main__':
  orange = Money(100)
  orange.display().add(300).display().add(80).display()

## 4.5 集合物件

# %load ex04-09.py
class Person():
  pname = None

  def getName(self):
    return self.pname

  def setName(self, value):
    self.pname = value


class Baseball_team():
  manager = None
  coach = None
  players = []

  def __init__(self):
    self.manager = Person()
    self.coach = Person()
    self.idx = 0

  def setManager(self, m):
    self.manager.setName(m)

  def setCoach(self, c):
    self.coach.setName(c)

  def addPlayer(self, name):
    p = Person()
    p.setName(name)
    self.players.append(p)
    self.idx += 1

  def display(self):
    print("Manager: ", self.manager.getName())
    print("Coach: ", self.coach.getName())
    print("")
    print("Players: ")
    for i in range(0, self.idx, 1):
      print(" ", self.players[i].getName())


if __name__ == '__main__':
  RedSock = Baseball_team()
  RedSock.setManager("James Lin")
  RedSock.setCoach("David Wang")
  RedSock.addPlayer("Jim Lin")
  RedSock.addPlayer("Alvin Kao")
  RedSock.addPlayer("John Coppin")
  RedSock.display()