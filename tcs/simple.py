N = int(input("enter the number of students to be selected"))
K = int(input("enter the number of students you want to select"))


def find_max(list_):
    max1 = max(list_)
    return max1
    
    
    
max_list = []

len_list = []
for i in range(N):
    item = int(input())
    len_list.append(item)
    
print(len_list)
    

    
for i in range(K):
    max1 = find_max(len_list);
    print(max1)
    
    max_list.append(max1)
    len_list.remove(max1)
    

print(sum(max_list))