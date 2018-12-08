str="siiiiiiiiiiidddddddddddddduuuuuuuuuuuuuu"
dict={}
for x in str:
    dict[x]=dict.get(x,0)+1
for k,v in dict.items():
    print("letter={}      occurences={}".format(k,v))