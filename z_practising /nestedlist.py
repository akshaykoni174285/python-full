list_inner=[]
list_name = []
marks_list=[]
list_outer = []
for i in range(int(input())):
    for k in range(1):
        list_inner.append(input("name:"))
        marks=float(input("marks:"))
        list_inner.append(marks)
        marks_list.append(marks)

    list_outer.append(list_inner)
    list_inner=[]


# find the lowest and remove it from the list
list_outer.pop(marks_list.index(min(marks_list)))
marks_list.pop(marks_list.index(min(marks_list)))
    
second_min = min(marks_list)
# count_acc = marks.count(second_min)


for i in range(len(list_outer)):
    if second_min == list_outer[i][1]:
        list_name.append(list_outer[i][0])
        
    
list_name.sort()
for i in list_name:
    print(i)
    

        
     
        
        
    
    

    

    
    
    

