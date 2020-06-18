a=[];b=[]
for i in range(6):
    num=int(input("Enter number in list 1 "))
    a.append(num)
for j in range(6):
        num2=int(input("Enter number in list 2 "))
        b.append(num2)

for x in range(6):
    a[x] = a[x] + b[x]
    b[x] = a[x] - b[x]
    a[x] = a[x] - b[x]

print(a,b)
