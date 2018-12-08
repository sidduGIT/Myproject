d1 = {'a': 100, 'b': 200, 'c':300,'d':50,'e':150,'f':400,'g':600}
d1list=[]
for v in d1.values():
    d1list.append(v)
slist=sorted(d1list)
print(slist)
print("first highest",slist[-1])
print("second highest",slist[-2])
print("third highest",slist[-3])

print("lowest=",slist[0],"highest=",slist[-1])