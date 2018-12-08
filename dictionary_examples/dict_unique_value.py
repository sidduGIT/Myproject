list1=[{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, {'VII': 'S005'}, {'V': 'S009'},
 {'VIII': 'S007'},{'X':'S010'}]
print("original list of dict",list1)
d1=[]
for dic in list1:
    for v in dic.values():
        if v not in d1:
            d1.append(v)
print("list of unique values",d1)