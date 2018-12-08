dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
dic5={}
dic6={}
dic4.update(dic1)
dic4.update(dic2)
#dic4.update(dic3)
print(dic4)
for i in (dic1,dic2,dic3):
    dic4.update(i)
print(dic4)