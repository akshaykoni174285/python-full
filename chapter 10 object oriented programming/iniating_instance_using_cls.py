import csv

class Item():
    paycheck=0.8 #ths will give a discount of 20 percentatge
    name=""
    price=0
    quantity=0
    all=[]
    def __init__(self, name, price:float, quantity=0):
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
        
        
    @classmethod
    def initialize_from_csv(cls):
        with open('/home/whoami/Documents/python/Python Full/chapter 10 object oriented programming/item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity"))
            )      

        
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
        
        
Item.initialize_from_csv()
print(Item.all)