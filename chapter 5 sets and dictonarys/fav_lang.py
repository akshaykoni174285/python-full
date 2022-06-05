lang_dit = {}
names = ["akshay","eren","itadori","gojo","mikasa","izumi miyamura"]
for student in range(6):
    sub  = input(f"enter the fav subject of {names[student]} :")
    lang_dit[names[student]] = sub
    
    
print(f"the list of the subject is : ",lang_dit)