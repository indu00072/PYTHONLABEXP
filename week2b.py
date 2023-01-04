""" AIM :Write a python script to read four integer values separated with commas and 
         display the sum of those four numbers """
# SOURCE CODE :
a=list(input("enter the efourr integers").split(","))
sum=0
for x in range(0,4):
    sum+=int(a[x])
print("the sum of four integers is :",sum)


"""INPUT :
           enter the efourr integers 1,2,3,4
OUTPUT :
           the sum of four integers is : 10

RESSULT :The above program has been exicuted succefully ."""
