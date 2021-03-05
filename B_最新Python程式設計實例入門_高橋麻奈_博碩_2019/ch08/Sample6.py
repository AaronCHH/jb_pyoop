import myclass

pr = myclass.Customer("鈴木", 23, "mmm@nnn.nn.jp", "xxx-xxx-xxxx")

nm = pr.getName()
ag = pr.getAge()
ad = pr.getAdr()
tl = pr.getTel()

print(nm, "先生/小姐", ag, "歲。")
print("E-mail：", ad, "電話號碼：", tl, "。")