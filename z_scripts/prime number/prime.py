# result= False
# def prime(number):
#     if (number%number)==0:
#         for i in range(2,101):
#             if (number%i)==0:
#                 result = True
#             else:
#                 result = False
                
#     if (result==True):
#         print("the number is not prime number")
#     else:
#         print("the number is prime number")
        
                

# num = int(input("enter a number : "))
# prime(num)

        
        
def prime(num):
    is_prime=True
    for i in range(2, num):
        if (num%i)==0:
            is_prime = False
        
    if is_prime == True:
        print("num is prime number")
    else:
        print("num is not prime number")
                
number = int(input("enter a number : "))
prime(number)