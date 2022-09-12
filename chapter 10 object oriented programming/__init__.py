# lets implement a class 

from unicodedata import name


class Item():
    name
    price=0
    quantity=0
    # here the attributes will come and we will be adding them later
    
    # lets define a contructor that will initialize the attributes for different instances 
    # def __init__(self, name, price, quantity):  now here everything is fine but what if another daya type is passed then it will behave differently 
    def __init__(self, name:str, price:float, quantity=0):
        # using assert for validation of values that have been passed to __init__
        assert price<0, f"the value of price {price} cant be in negative"
        assert quantity<0, f"the value of price {quantity} cant be in negative"
        
        # contructing values
        self.name = name
        self.price = price
        self.quantity=quantity
    
    def Calculate_the_ammount(self): # now keep in mind that you have to provide self everytime that is passed automatic
        
        # return price*quantity      # now as we are using contructor we dont need to use or pass the arguments one more time to compute the ammount
        return self.price * self.quantity
        
        
item1 = Item("phone",1000,4)
print(item1.Calculate_the_ammount(item1.price,item1.quantity))

item2 = Item("laptop",2000,4)


# item1.has_nun_pad = False 
# now if we havent used the attribute then it doesnt mean we cant not create attributes even if its not declared inside the class `
# 
# `