import datetime

current_date = datetime.datetime.now()
name = input('enter your naem: ')

print(f''' Dear {name}
            you are selected
            {current_date.strftime("%6x")}''')