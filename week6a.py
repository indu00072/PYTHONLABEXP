n=int(input("enter how many student details you need to store: "))
print(n)
list=[]
for i in range(0,n):
    list.append([])
    name=input("enter name: ")
    list[i].append(name)
    roll=input("enter id: ")
    list[i].append(roll)
    branch=input("enter branch: ")
    list[i].append(branch)
    age=input("enter age:  ")
    list[i].append(age)
list.sort()
for i in range(0,n):
    for j in range(4):
        print(list[i][j],end=" ")
    print()
