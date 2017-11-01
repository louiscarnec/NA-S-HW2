# -*- coding: utf-8 -*-9
"""
Spyder Editor

This is a temporary script file.
"""
import timeit
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from decimal import Decimal as D
from fractions import Fraction as F
from sympy import *

def theSum(init=0, end=0):
    result=0
    while init <= end:
        result = result + init
        init += 1
    return result

#run = timeit.timeit(lambda: theSum(0,10), number=10)    
#run1 = timeit.timeit(lambda: theSum(0,10), number=100)
IntegerList = [3.98473243877e-05,0.000419604400577,0.00200987489188,0.0313006770421,0.28569263706
, 1.95032789518,4.03597066271]
IntegerList1 = [0.000323608573694, 0.00221997896546,0.0251116630704,
               0.224708722096,2.70572147203,18.2572223275,38.0584542136]

#run = timeit.timeit(lambda: theSum(0.0,10.0), number=10)               
#run1 = timeit.timeit(lambda: theSum(0.0,10.0), number=100)
FloatingPointList = [0.000124975699237,0.000724496806924,0.00746412835178,0.0395852980278
, 0.409503707612, 1.98173845424, 3.83093263266]
FloatingPointList1 = [0.00105655784319,0.00373659228103,0.0494106822223,0.374828082945
,3.68944323628,17.8895178595,35.9459682356]

#run = timeit.timeit(lambda: theSum(D(0),D(500000)), number=10)
#run1 = timeit.timeit(lambda: theSum(D(0),D(10)), number=100)
DecimalList = [0.0309988033728,0.142998764733, 1.15926613303,11.7853503123,119.761405693,633.844415518
]
DecimalList1 = [0.145675780434,1.19396288886,11.8938720853,123.059856719,1433.33609467,]

#run = timeit.timeit(lambda: theSum(F(0,1),F(1000000,1)), number=10)
#run1 = timeit.timeit(lambda: theSum(F(0,1),F(500000,1)), number=100)
FractionList = [0.0065663560581,0.0842408662083,0.515851990132,5.01664410664,55.5547610911,300.071553116]    
FractionList1 = [0.0588273294686, 0.514672871579,5.14962066555,54.5055224769, 534.883679019,]               

#run = timeit.timeit(lambda: theSum(sqrt(1),sqrt(1000000)), number=10)
SymbolicList = [0.0248013369383,0.0276836267349,0.307705265039,0.119238288207,1.79869131727
,2.80614578566,0.413982909122]

print IntegerList
print FloatingPointList
print DecimalList
print FractionList
print SymbolicList

#print run
#print run1

fig = plt.figure()
plt.plot(IntegerList,'bo',FloatingPointList, 'go',DecimalList, 'yo',FractionList,'g^',SymbolicList,'r^',linestyle='-')
plt.axis([-1,7,0,700])
plt.xticks(arange(7), ('10^1','10^2','10^3','10^4','10^5','5*(10^5)','10^6'), size='small')
plt.xlabel('n')
plt.ylabel('Times (seconds)')
plt.title('Sum Runtime')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.show()   

#plt.plot(IntegerList, 'ro',FloatingPointList,'g^',DecimalList,'yo',FractionList, 'b^')
#plt.axis([0,6,0,1500])
#plt.show()  

plt.plot(IntegerList,'bo',FloatingPointList, 'go',SymbolicList, 'ro',linestyle='-')
plt.axis([0,7,0,5])
plt.xticks(arange(7), ('10^1','10^2','10^3','10^4','10^5','5*(10^5)','10^6'), size='small',)
plt.xlabel('n')
plt.ylabel('Times (seconds)')
plt.title('Sum Runtime: Excluding Decimal and Fraction')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.show()            




