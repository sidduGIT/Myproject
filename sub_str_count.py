str="I live in India, India is a great country"
sub_str='India'
count=0
sub_len=len(sub_str)
for i in range(len(str)):
    if str[i:i+sub_len]==sub_str:
        count+=1
print(count)
