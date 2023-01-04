""" Write a python script to calculate electricity bill based on following slab 
rates.
Consumption units Rate (in Rupees/Unit)
0-100 4
101-150 4.6
151-200 5.2
201-300 6.3
Above 300 8
(Hint: To get Consumption units take current meter reading and old meter 
reading from the user as input  """

# source code :

cunit=int(input("enter the currrent meter reading units "))
ounit=int(input("enter the old meter reading units "))
cspunits=cunit-ounit
print("the consumption units are :",cspunits)
if cspunits>=0 and cspunits<=100:
    electricitybill=cspunits*4
elif cspunits>=101 and cspunits<=150:
    electricitybill=cspunits*4.6
elif cspunits>=151 and cspunits<=200:
    electricitybill=cspunits*5.2
elif cspunits>=201 and cspunits<=300:
    electricitybill=cspunits*6.3
else:
    electricitybill=csunits*8;
print("The electricity bill is:",electricitybill)


"""INTPUT :
            enter the currrent meter reading units : 500
            enter the old meter reading units      : 350
OUTPUT :

            the consumption units are : 150
            The electricity bill is: 690.0
            
RESULT : The above program has been exicuted successfully ."""

     
