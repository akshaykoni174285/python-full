count = 0
flag = True;
add_list = []
while flag == True:
    i = int(input("enter a number you want to add: "))
    add_list.append(i)
    question = input("do you want to continue?")
    if question.lower() == "y":
        flag = True;
    elif question.lower() == "n":
        flag = False;
    else:
        print("enter a appropriate answer")
        flag = True;
        count+=1
        if count == 3:
            print("exiting a program you didnt provide a correct answer")
            exit()

# sum_list = add_list.sum()

print("the sum of the numbers is :",sum(add_list))
    
            
        
        
        