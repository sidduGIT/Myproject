dic={1:2,3:4,5:6}
key=int(input("enter a key element"))
if key in dic:
    print("key present")
else:
    print("key NOT present")
for k,v in dic.items():
    print(k,v)
n=int(input("enter n"))
dic1={}
for i in range(1,n+1):
    dic1[i]=i**2
print(dic1)