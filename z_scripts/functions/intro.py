def square(num):
    print(num*num)
    
    
bool = False

while bool is not True:
    number = int(input('enter the number: '))
    square(number)
    question = input('do you want to continue? (y/n): ')
    
    if (question == 'y'):
        continue
    else:
        bool = True     