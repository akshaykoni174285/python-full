

class Item():
    paycheck = 0.8
    
    def __init__(self,name:str,value:float,quantity:int):
        
        assert value>=0, f"the value of value cant be negative"
        assert value>=0, f"the value of quantity cant be negative"
        
        
        self.name = name
        self.value = value
        self.quantity = quantity
        
    def getvalue(self):
        return self.value * self.quantity
        
        
item1 = Item("laptop",2000,5)
value1 = item1.getvalue()
print(value1)
