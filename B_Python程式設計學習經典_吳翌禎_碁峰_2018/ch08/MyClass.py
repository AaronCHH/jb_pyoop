#-------------------------------
#   Car.py   
#-------------------------------
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




















	


