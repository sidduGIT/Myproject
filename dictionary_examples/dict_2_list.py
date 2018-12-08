food = {'pizza': 324, 'sandwich': 78, 'hot dog': 90}
klist=[]
vlist=[]
for k,v in food.items():
    klist.append(k)
    vlist.append(v)
print("keys list",klist)
print("values list",vlist)

klist=['pizza', 'sandwich', 'hot dog']
vlist=[324, 78, 90]
dict1=dict(zip(klist,vlist))
print(dict1)