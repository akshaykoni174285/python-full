num1 = int(input("Enter number: "))
flag = 0
for i in range(1,num1+1):
    if num1%i == 0:
        flag += 1
        
        
if flag<3:
    print(f"{num1} is prime")
else:
    print(f"{num1} is not a prime")