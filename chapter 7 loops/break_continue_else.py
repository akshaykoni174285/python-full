# break in for loop 

for i in range(9):
    print(i)
    if i == 4:
        break
    # this will come out of the loop when i is 4

# continue is used to skip a itteratin for a specific number

for i in range(7):
    if i != 4:
        print(i)
    else:
        continue