#-----------------------------------
#   CH_8_4_EX_1_Encapsulation_1.py   
#-----------------------------------
class Human: 
   def __init__(self, height, weight): 
      self.__height=height
      self.__weight=weight
   def BMI(self): 
      return self.__weight / ((self.__height/100)**2)

#-----建立物件
model_Bill = Human(180, 88) 

#-----使用物件方法
print(model_Bill.BMI())






















	


