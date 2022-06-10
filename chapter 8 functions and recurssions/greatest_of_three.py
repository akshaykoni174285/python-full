

def greatest_of_three(n1,n2,n3):
    
    
    if n1 > n2:
        if n1 > n3:
            print(f"the greatest number among {n1} {n2} and {n3} is {n2} and {n1}") 
        else:
            print(f"the greatest number among {n1} {n2} and {n3} is {n2} and {n3}")
    print(f"the greatest number among {n1} {n2} and {n3} is {n2} and {n2}") 


greatest_of_three(2,3,6)
   