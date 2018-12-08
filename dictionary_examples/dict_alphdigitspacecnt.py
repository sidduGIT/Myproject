s="HellO WorLd! 123"
dic={"digits":0,"alpha":0,"space":0,"space":0,"upper":0,"lower":0,"alphanum":0}
for i in s:
    if i.isdigit():
        dic["digits"]+=1
    #elif i.isalpha():
     #   dic["alpha"]+=1
    elif i.isspace():
        dic["space"]+=1
    elif i.isupper():
        dic["upper"]+=1
    elif i.islower():
        dic["lower"]+=1
    #elif i.isalnum():
     #   dic["alphanum"]+=1

print(dic)
for k,v in dic.items():
    print(k,v)
print("digits=  ",dic["digits"])
print("alpha=  ", dic["alpha"])
print("space=  ", dic["space"])
print("upper=  ", dic["upper"])
print("lower=  ", dic["lower"])
print("alphanum=  ", dic["alphanum"])


'''
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1

print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])'''