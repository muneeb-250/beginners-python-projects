#First Program:
def check_armstrong():
    str_num=str(num)
    length=len(str_num)
    output=0
    temp=num
    for i in range(length):
        output+=int(str_num[i])**length
    return output

num=int(input("Enter number: "))
armstrong=check_armstrong()
if num==armstrong:
    print("It's an armstrong number")
else:
    print("It's not an armstrong number")
    
    
#Second Program:
def check_armstrong():
    output=0
    temp=num
    while temp>0:
        digit=temp%10
        output+=digit**len(str(temp))
        temp//=10
    return output

num=int(input("Enter number: "))
if num==check_armstrong():
    print("It's an armstrong number")
else:
    print("It's not an armstrong number")