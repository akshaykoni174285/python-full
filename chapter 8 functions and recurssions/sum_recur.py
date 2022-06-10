

def sum_recur(num1):
    sum = 0
    if num1 <=1:
        sum += 0
    else:
        sum = num1 + sum_recur(num1-1)
    return sum


num1 = int(input("enter a number :"))
val = sum_recur(num1)
print(val)
