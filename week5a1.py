n=input("enter spaced integers:")
a=tuple(int(num) for num in n.split())
b=list(a)
for i in range(0,len(a)-1):
    if(b[i]>b[i+1]):
        b[i]=b[i+1]
    else:
        b[i]=-1
b[len(a)-1]=-1
a=tuple(b)
print(a)

    
        
