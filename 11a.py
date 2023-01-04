try:  
    a = 10/0  
    print (a)
except ArithmeticError:  
        print ("This statement is raising an arithmetic exception.")
else:  
    print ("Success.")
try: 
    b = [1, 2, 3] 
    print (b[3]) 
except LookupError: 
    print ("Index out of bound error.")
else: 
    print ("Success")
try:
    array = { 'a':1, 'b':2 }
    print (array['c'])
except LookupError: 
    print ("key out of bound error.")
else: 
    print ("Success")

import module_does_not_exist
