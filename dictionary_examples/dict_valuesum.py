dict1={'a': 1, 'b': 2, 'c': 3, 'd': 3, 'z': 26, 'y': 25, 'x': 24}
sum=0
for i in dict1.values():
    sum+=i
len1=len(dict1)
avg=sum//len1
print("sum of values present in dict",sum)
print("length of dict",len1)
print("avg of values present in dict",avg)