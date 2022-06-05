spam = ["fuck","cunt","bastard","silly","whore","slut","dog"]

messgae = input("enter a text message: ")
split_message = messgae.split(" ")

for i in spam:
    if i in split_message:
        split_message.remove(i)
        final_message = "".join(split_message)
        
        

print(final_message)
        
        

    