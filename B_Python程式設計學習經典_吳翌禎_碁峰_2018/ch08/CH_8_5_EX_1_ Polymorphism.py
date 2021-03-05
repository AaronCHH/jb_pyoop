#---------------------------------
#   CH_8_5_EX_1_ Polymorphism.py   
#---------------------------------
class Mymath:
     def getArea(self, radiusorbase, height=None):
         if height is not None:
            return (radiusorbase * (height / 2));
         else:
            return (3.14 * (radiusorbase * radiusorbase));
 
#-----建立物件
obj = Mymath()
 
#-----輸入兩個參數呼叫方法計算三角形面積
print(obj.getArea(10,10))
 
#-----輸入一個參數呼叫方法計算圓形面積
print(obj.getArea(5))























	


