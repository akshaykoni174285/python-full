# find the doubel space in a string 

str = "this is a normal string that contains double  spaces"

print(str.find("  "))

str = str.replace("  ", " ")
print(str)