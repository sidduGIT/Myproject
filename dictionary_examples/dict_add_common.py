d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 200, 'b': 300, 'd':400}
d3={}
for k1,v1 in d1.items():
    for k2,v2 in d2.items():
        print(k1,v1)
        print(k2, v2)
        if k2==k1:
            #d3[k1]=d1[k1]+d2[k2]
            d3[k1]=v1+v2
            print(d3[k1])
else:
    d3[k1]=v1
    d3[k2]=v2
print(d3)

from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3=Counter(d1)+Counter(d2)
print(d3)