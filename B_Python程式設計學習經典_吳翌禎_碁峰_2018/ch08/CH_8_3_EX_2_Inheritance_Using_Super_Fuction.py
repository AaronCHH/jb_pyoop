#---------------------------------------------------
#   CH_8_3_EX_2_Inheritance_Using_Super_Fuction.py   
#---------------------------------------------------
from MyClass import Car
class Truck(Car):
#----- 新增loading載重屬性
   def __init__(self, brand, model, seats, cc, loading): 

#----- 使用super()
      super().__init__(brand, model, seats, cc) 
      self.loading = loading




















	


