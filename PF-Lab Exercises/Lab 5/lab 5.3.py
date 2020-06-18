a=input("Enter your name: ")
b=int(input("Enter the no. of first characters you want in lowercase: "))
print(a.lower()[0:b]+a.upper()[b:])