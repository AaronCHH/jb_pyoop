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
