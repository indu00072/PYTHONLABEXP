"""AIM:Writeapython scripttoperformfollowingsetsoperations.
       i)update () ii)discard() iii)issuperset() iv)isdisjoint() 
       v) symmetric_difference ()"""
#PROGRAM:

A = {'a', 'b'}
B = {1, 2, 3}
A.update(B)
print(A)
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)
s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(s1.isdisjoint(s2))
p = {"apple", "banana", "cherry"}
q = {"google", "microsoft", "apple"}
r = p.symmetric_difference(q)
print(r)

"""OUTPUT :
{1, 2, 3, 'b', 'a'}
{'apple', 'cherry'}
True
True
{'microsoft', 'cherry', 'banana', 'google'} 

RESULT : The above program has been exicuted successfully . """

