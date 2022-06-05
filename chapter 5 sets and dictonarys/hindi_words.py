
hindi_dictionary = {
    "Pankha":"Fan",
    "chuha":"rat",
    "baksa":"box"
}

print(hindi_dictionary)
print("options are :",hindi_dictionary.keys())
name = input("enter the word of which you want to find the meaning: ")
print(f"the meaning of the {name} in english is {hindi_dictionary[name]}")
