# lets implement a class 


class Item():
    paycheck=0.8 #ths will give a discount of 20 percentatge
    name=""
    price=0
    quantity=0
    all=[]
    # here the attributes will come and we will be adding them later
    
    # lets define a contructor that will initialize the attributes for different instances 
    # def __init__(self, name, price, quantity):  now here everything is fine but what if another daya type is passed then it will behave differently 
    def __init__(self, name:str, price:float, quantity=0):
        # using assert for validation of values that have been passed to __init__
        assert price>=0, f"the value of price {price} cant be in negative"
        assert quantity>=0, f"the value of price {quantity} cant be in negative"
        
        # contructing values
        self.name = name
        self.price = price
        self.quantity=quantity
        
        # appending the instances in a list 
        Item.all.append(self)
    
    def Calculate_the_ammount(self): # now keep in mind that you have to provide self everytime that is passed automatic
        
        # return price*quantity      # now as we are using contructor we dont need to use or pass the arguments one more time to compute the ammount
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.paycheck
        
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
        
        
item1 = Item("phone",1000,4)
# print(item1.Calculate_the_ammount())
# item1.apply_discount()
# print(item1.price)

item2 = Item("laptop",2000,4)
# print(Item.paycheck)
# print(Item.__dict__) #now we can access through the class and also through the instance 
# lets see how 
# print(item1.paycheck)
# print(item1.__dict__)
# when you print above statement then you will see you wont find the paycheck 
""" explaination 
    now the instance item1 doesnt have the attribute paycheck and thats why it searches from the class itlself and thats why its able to access it 
    
    now to check what all attributes a instance or a class can access then you can use __dict__
    """
# print(item2.paycheck)
item3 = Item("printer",4000,2)
item4= Item("keyboard",2000,1)
items = Item("mouse",500,6)
print(Item.all)




# item1.has_nun_pad = False 
# now if we havent used the attribute then it doesnt mean we cant not create attributes even if its not declared inside the class `
# 
# `