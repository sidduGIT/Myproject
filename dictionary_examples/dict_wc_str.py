str="siddu siddu santu atharv siddu atharv santu"
words=str.split(" ")
count=[]
for word in words:
    c=words.count(word)
    count.append(c)
print(words)
print(count)
dict1=dict(zip(words,count))
print(dict1)

count={}
for word in words:
    if word in count:
        count[word]=count[word]+1
    else:
        count[word] =1
print(count)