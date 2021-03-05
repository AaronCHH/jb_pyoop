#-------------------------------------
#   CH_8_2_EX_3_Object_Creation_2.py   
#-------------------------------------
class Car: 
   def __init__(self, brand, model, seats, cc): 
      self.brand=brand
      self.model=model
      self.seats=seats
      self.cc=cc
   def display(self): 
      s="品牌:"+self.brand+ "\r\n";
      s = s + "型號:" + self.model + "\r\n"; 
      s = s + "規格:" +self.seats + "座位" + self.cc + "CC";
      return s

#建立物件
mycar1 = Car("Nissan", "X Trail", "4", "2400" ) 

# 使用物件方法
print(mycar1.display())




















	


