dict1={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
'''vsum=0
ksum=0
for v in dict1.values():
    vsum=vsum+v
print(" sum", vsum) #sum of all values

for k in dict1.keys():
    ksum=ksum+k
print(" sum", ksum) #sum of all values

for k,v in dict1.items():
    print("key",k,"value",v)

v1=int(input("enter the values to be searched"))
for v in dict1.values():
    if v1==v:
        print("value present")
        exit()
else:
    print("value NOT present")
k1=int(input("enter key toget its value"))
if k1 in dict1:
    print("key",k1,"value is",dict1[k1])
else:
    print("key entered NOT found")
print(dict1.keys())
print(dict1.values())

klist=dict1.keys()
vlist=dict1.values()
print(klist)
print(vlist)'''
mul=1
for v2 in dict1.values():
    mul=mul*v2
print("multiplication of values",float(mul))
