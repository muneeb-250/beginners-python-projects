word=input('Enter word')
d1={}
for i in word:
    if i in d1:
        d1[i]+=1
    else:
        d1[i]=1
print(d1)




