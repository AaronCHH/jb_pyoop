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

print(pr1.getName(), "先生/小姐", pr1.getAge(), "歲。")
print(pr2.getName(), "先生/小姐", pr2.getAge(), "歲。")
print("合計人數為", Person.getCount(), "人。")
