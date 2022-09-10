character = input().lower()
new_letters = []
letters = ['a', 'b','c','d','e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n','o', 'p']

for i in character:
    if i in letters:
        new_letters.append(i)
        
letters_16 = new_letters[:16]
enc = ""
letters_16 = "".join(letters_16)

for i in letters_16:
    if i in letters_16[0:8]:
            enc = enc+"0"
            if i in letters_16[0:4]:
                enc = enc+"00"
                if i in letters_16[0:2]:
                    enc = enc+"000"
                    if i in letters_16[0]:
                        enc = enc+"0000 "
                    elif i in letters_16[-1]:
                        enc = enc+"0001 "
                elif i in letters_16[2:4]:
                    enc = enc+"001"
            elif i in letters_16[8:]:
                enc= enc+"01"
    else:
        enc = enc+"1"
        if i in letters_16[8:12]:
            enc = enc+"10"
            if i in letters_16[8:10]:
                enc = enc+"100"
                if i in letters_16[8]:
                    enc = enc+"1000 "
                elif i in letters_16[-1]:
                    enc = enc+"1001 "
            elif i in letters_16[10:12]:
                enc = enc+"101"
        else:
            enc = enc+"11"
    # for j in range(4):
        
            
        
        
print(bin(16))
# print(enc[len(enc) - 64:])
print(enc)