lst=[x for x in input("Enter strings separated by, \n").split(',')]
l=len(lst)
for i in lst:
    cnt=0
    for j in lst:
        if i==j:
            cnt+=1
        if(cnt>1):
            lst.remove(i)
lst.sort()
print("after removing : \n",lst)
