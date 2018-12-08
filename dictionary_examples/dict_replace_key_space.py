dct={"ab cd":1,"efg hi":2,"jk lmno":3}
print("before replacng space in keys",dct)
dct1={}
for k,v in dct.items():
    dct1[k.replace(' ','')]=v
print("after replacng space in keys",dct1)

dct={1:"ab cd",2:"efg hi",3:"jk lmno"}
print("before replacng space in values",dct)
dct1={}
for k,v in dct.items():
    dct1[k]=v.replace(' ','')
print("after replacng space in values",dct1)