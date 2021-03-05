#-------------------------------------------------------
#   CH_8_3_EX_2_Inheritance_Using_Override_Function.py   
#-------------------------------------------------------
from MyClass import Car
class Truck(Car):
#-----新增loading載重屬性
   def __init__(self, brand, model, seats, cc, loading): 

#-----使用super()
       super().__init__(brand, model, seats, cc) 
       self.loading = loading

#-----覆寫display()方法
   def display(self): 
       s = "本卡車是" + self.brand +" "+self.model + "\r\n";
       s = s + self.cc + "CC" + "\r\n"; 
       s = s + "目前重量為" + self.loading + "噸" + "\r\n"; 
       return s

#-----建立物件
mycar1 = Car("Nissan", "X Trail", "4", "2400" ) 
mytruck1 = Truck("Ford", "F-150", "2", "2700", "2.2" )

#-----使用物件方法
print(mycar1.display())
print("-"*30)
print(mytruck1.display())





















	


