
def to_farehnite(cel):
    return (cel *(9/5) + 32)

cel = float(input("enter the temperature in celcius"))

val = to_farehnite(cel)
print(f"the temperature in celcius is {val} in farehnite")