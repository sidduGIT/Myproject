d='w3resource w3resource w3resource'
dct={}
for char in d:
    if char in dct:
        dct[char]=dct[char]+1
    else:
        dct[char]=1
print(dct)
for k,v in dct.items():
    print(k,v)