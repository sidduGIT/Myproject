lst=[1,3,2,5,24,17,13,20,29]
edic={}
odic={}
for i in lst:
    if(i%2==0):
        edic[i]=i*i
    else:
        odic[i]=i*i*i
print(edic)
print(odic)