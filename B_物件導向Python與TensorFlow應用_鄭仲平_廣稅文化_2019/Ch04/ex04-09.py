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
