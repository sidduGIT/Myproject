num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
print("before sorting",num)
new_num={}
for k,v in num.items():
    new_num[k]=sorted(v)
print("after sorting",new_num)

num = {'n1':'bca', 'n2':'efd','n3':'hgi'}
sort_num={}
tstr=''
for k,v in num.items():
    tstr=sorted(v)
    sort_num[k]=" ".join(tstr)
print(sort_num)