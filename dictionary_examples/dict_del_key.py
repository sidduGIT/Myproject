dict1={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
del(dict1[2])
print(dict1)
del(dict1[5])
print(dict1)

dict2={'c':3,'b':2,'a':1,'z':31,'f':7,'k':10}
kdict3={}
vdict4={}
for k in sorted(dict2):
    kdict3[k]=dict2[k]
    #print("key",k,"value",dict2[k])
print(kdict3)

for v in sorted(dict2.values()):
    print(v)
    #vdict4[k]=dict2[k]
lst1=['c','d','h','j','f']
lst2=[4,1,7,9,10]
dict5=dict(zip(lst1,lst2))
print(dict5)
print("maximu of dict5",dict5[max(dict5)])
print("mnimum of dict5",dict5[min(dict5)])
