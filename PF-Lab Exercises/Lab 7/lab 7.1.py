age=int(input("Enter age# "))
if age<2:
    print("The Person is a baby.")
elif age>=2 and age<4:
    print("The Person is a toddler.")
elif age>=4 and age<13:
    print("The Person is a kid.")
elif age>=13 and age<20:
    print("The Person is a teenager.")
elif age>=20 and age<65:
    print("The Person is an adult.")
elif age>=65:
    print("The Person is an elder.")