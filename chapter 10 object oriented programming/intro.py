# lets implement a class 

from unicodedata import name


class Item():
    name
    price=0
    quantity=0
    # here the attributes will come and we will be adding them later
    
    def Calculate_the_ammount(self,price,quantity):
        return price*quantity
        
        
item1 = Item()
item1.name = "laptop"
item1.price = 10000
item1.quantity = 2
print(item1.Calculate_the_ammount(item1.price,item1.quantity))

