l1 = [23,56,78,56,32]
print(l1)
temp = l1[0]
l1[0]=l1[-1]
l1[-1]=temp
print(l1)