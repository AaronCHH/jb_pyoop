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
