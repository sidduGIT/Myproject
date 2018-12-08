dict1={'a': 1, 'b': 2, 'c': 3, 'd': 3, 'z': 26, 'y': 25, 'x': 24}
num=int(input("enter a number which is to be multiplied"))
for k,v in dict1.items():
    dict1[k]=num*v
print("dictionery after multiplying",dict1)