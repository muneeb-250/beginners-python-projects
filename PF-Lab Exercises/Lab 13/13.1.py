num=int(input('Enter number of employees: '))
data=[]
for i in range(num):
    temp=[]
    for d in  range(1):
        id=input('Enter ID: ')
        name=input("Enter name: ")
        salary=input("Enter salary: ")
        temp.append(id)
        temp.append(name)
        temp.append(salary)
        data.append(temp)

file =open("employee.txt",'wt')
for files in data:
    file.write("ID: "+files[0]+"\nName: "+files[1]+"\nSalary: "+files[2]+"\n")
file.close()

try:
    file=open("employee.txt","rt")
    print(file.read())
except FileNotFoundError:
    print("File not found")
else:
    file.close()





