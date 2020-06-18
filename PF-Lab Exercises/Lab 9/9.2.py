a=[7,3,5,2,1,2]
b=[]
for x in range(len(a)):
    min=a[0]
    for num in a:
        if  num < min:
            min = num
    b.append(min)
    a.remove(min)
print(b)



