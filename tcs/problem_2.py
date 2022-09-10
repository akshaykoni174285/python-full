num_list = []
flag = True

size = int(input())
val = input()
print(val)
for i in val:
    num_list.append(int(i))


while flag:
    
    num1= num_list[0]
    avg = sum(num_list)/len(num_list)
    num_list[0]=avg
    num2 = num_list[0]
    if num2 < num1:

    
        print("NO")
        flag = False
    else:
        print("yes")
        flag = False
    
    