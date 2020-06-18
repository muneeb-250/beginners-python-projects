n=int(input("Enter no. of terms: "))
a=1;b=2
print(a,end=',')
print(b,end=',')
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c,end=',')