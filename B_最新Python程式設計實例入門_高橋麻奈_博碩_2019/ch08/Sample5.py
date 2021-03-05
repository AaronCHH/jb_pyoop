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
