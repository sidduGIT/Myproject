str="hai i am siddu siddu siddu siddu is a good guy"
lst=str.split(" ")
dic={}
for i in lst:
    if i in dic:
        dic[i]=dic[i]+1
    else:
        dic[i]=1
print(dic)
max=1
for v in dic.values():
    if v>max:
        max=v
print("maximum number",max)



