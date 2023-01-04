 """ AIM :Write a python script to evaluate following expressions by considering necessary inputs.
          i) ax2 + bx + c ii) ax5 + bx3 + c iii) (ax + b) / (ax – b) iv) x – a / b + c """
 
#SOURCE CODE:
a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
x=int(input("enter the value of x"))
p=a*x**2+b*x+c
q=a*x**5+b*x**3+c
r=(a*x+b)/(a*x-b)
s=(x-a)/(b+c)
print("the value of p:",p)
print("the value of q:",q)
print("the value of r:",r)
print("the value of s:",s)

""" INPUT :
            enter the value of a 1
            enter the value of b 2
            enter the value of c 2
            enter the value of x 3
 OUTPUT :
            the value of p: 17
            the value of q: 299
            the value of r: 5.0
            the value of s: 0.5

RESULT :The above program has been exicuted successfully ."""
