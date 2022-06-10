
number = int(input("enter a number: "))
fact = 1
for i in reversed(range(1,number+1)):
    fact = fact *i
    
print(f"the factorial of the num {number} is : {fact}")