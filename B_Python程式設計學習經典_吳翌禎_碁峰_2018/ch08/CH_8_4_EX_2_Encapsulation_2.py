#-----------------------------------
#   CH_8_4_EX_2_Encapsulation_2.py   
#-----------------------------------
class Human: 
   def __init__(self, height, weight): 
      self.__height=height
      self.__weight=weight
   def BMI(self): 
      return self.__weight / ((self.__height/100)**2)

#-----建立物件
model_Bill = Human(180, 88) 

#-----印出物件兩個屬性
print(model_Bill.__height) 
print(model_Bill.__weight)






















	


