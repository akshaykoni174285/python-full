
list_of_marks = []
for i in range(0, 6):
    marks = int(input(f"enter the marks of sub {i+1}: "))
    list_of_marks.append(marks)
    
    
list_of_marks.sort()
# you dont need to print this as it returns none 

print(list_of_marks)