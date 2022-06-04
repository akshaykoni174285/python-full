import random
letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't',
          'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I',
          'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y',
          'Z']
num_letters=0
num_symbols=0
num_numbers=0
rand_letters=[]
rand_symbols=[]
rand_num=[]
rand_password=[]
password=''
numbers = ['0','1','2','3','4','5','6','7','9']
symbols = ['!','#','$','%','&','(',')','*','+']
print("welcome to pypassword generator")
num_letters = int(input('how many letters you want in your password: '))
num_symbols = int(input('how many symbols you want in your password: '))
num_numbers = int(input('how many numbers you want in your password: '))

for count in range(num_letters):
    rand_letters.append(random.choice(letters))
    
for count in range(num_symbols):
    rand_symbols.append(random.choice(symbols))
    
for count in range(num_numbers):
    rand_num.append(random.choice(numbers))
    
random.shuffle(rand_letters)
random.shuffle(rand_num)
random.shuffle(rand_symbols)
rand_password = rand_letters+rand_num+rand_symbols
for i in range(5):
    random.shuffle(rand_password)
for i in rand_password:
    password = password+i
print(f"your password is : {password}")