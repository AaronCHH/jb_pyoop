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
