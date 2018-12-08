dict1={'a': 1, 'b': 2, 'c': 3, 'd': 3, 'z': 26, 'y': 25, 'x': 24}
key1=input("enter which key to remove")
for i in dict1.keys():
    if(i==key1):
        del dict1[key1]
        break
else:
    print("key is not found in the dictionery")

print("dictionery after removing given key-value pair",dict1)