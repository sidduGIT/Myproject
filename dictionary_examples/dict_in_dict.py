numbers = {}
letters = {}
comb = {}
numbers[1] = 56
numbers[3] = 7
letters[4] = 'B'
comb['Numbers'] = numbers
comb['Letters'] = letters
print(comb)

a = {}
a[1] = 1
a['1'] = 2
a[1.0]=4
count = 0
for i in a:
    count += a[i]
print(count)

import collections
a=collections.Counter([1,1,2,3,3,4,4,4])
print(a)

class demo(dict):
  def __test__(self,key):
    return []
a = demo()
a['test'] = 7
print(a)