n=int(input("enter n"))
while(n!=1):
    if n%2!=0:
        print("cannot be expresses ad power of two")
        break
    n=n//2
else:
    print("can be expressed as powerOfTwo")
