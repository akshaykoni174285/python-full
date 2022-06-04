# in this we will learn about slicing and indexing methods

# indexing 

name = "akshay"
# this is a string 

print(name[0])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

# so the counting start from the 0 in programming language 

# slicing 

print(name[0:0])  # this will print everything
print(name[3:])  # this will print everything starting from index 3 to the end 
print(name[3:5])  # this will print everything starting from index 3 to the index 5 but not including the 5
# output will be sha
print(name[::2])  # this will print everything but skips 1 space in between 
print(name[::-1])  # this will reverse the string 
