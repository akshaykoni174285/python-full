
# writing a function to greet a user 

def greet(name, *args, **kwargs):
    # print(f"hello {name} how are you")
    # you can use print or return based on the necessary
    return f"hello {name} how are you"
name = input("what is your name :")
val=greet(name)
print(val)

    