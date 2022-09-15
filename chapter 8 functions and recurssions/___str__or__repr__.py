class RandomNumber():
    
    def __init__(self,num):
        self.num = num
        
    def __str__(self):
        if self.num ==5:
            return f"five"
    # this helps to overrite the default use of __str__ that displays the memory address
    """ but we can customize the output """
    
    def __repr__(self):
        return f"RandomNumber({self.num})"
    
    # for representing we use __repr__
    
    
    # this kinda works like __str__ 
        
    
        
        
        
num1 = RandomNumber(5)
print(num1)