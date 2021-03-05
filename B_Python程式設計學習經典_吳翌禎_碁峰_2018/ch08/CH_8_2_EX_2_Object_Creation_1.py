#-------------------------------------
#   CH_8_2_EX_2_Object_Creation_1.py   
#-------------------------------------
class Human: 
    def __init__(self, height, weight): 
        self.height=height
        self.weight=weight
    def BMI(self): 
        return self.weight / ((self.height/100)**2)

#建立物件
model_Bill = Human(180, 88) 

# 印出物件兩個屬性
print(model_Bill.height) 
print(model_Bill.weight)

# 使用物件方法
print(model_Bill.BMI())




















	


