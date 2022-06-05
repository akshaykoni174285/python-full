flag = True
l_sub=[]
for i in range(3):
    sub = int(input(f"enter the marks for sub{i+1}"))
    if sub <= 100:
        l_sub.append(sub)
    else:
        print("the value is wrong plz try again")
        exit()
     
for i in l_sub:
    if i < 33:
        flag=False
        
if sum(l_sub)/len(l_sub) < 40:
    flag = False

for i in range(len(l_sub)-1):
    print(f"your marks for sub{i+1} is {l_sub[i]}")
    
print(f"your average percentage is {round(sum(l_sub)/len(l_sub))}")

if flag == False:
    print("sorry he failed this time work hard")
else:
    print("congo you are passed")
    