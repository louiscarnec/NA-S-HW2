# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 22:09:14 2015

@author: louiscarnec
"""

from decimal import getcontext, Decimal as D
from fractions import Fraction as F
import timeit 
import matplotlib.pyplot as plt
import sympy




def mysum(mylist, type1=''):
    s = 0.0
    if type1 == "decimal":
        s = D()
    if type1 == "fraction":
        s = F()
    for i in mylist: 
        s += i
    return s

def createlist(n, type1, precision=4):
    if type1 == "integer":
        Nlist = []
        for i in range(1, n+1):
            Nlist.append(i)
            
    if type1 == "floating":
        Nlist = []
        for i in range(1, n+1):
            Nlist.append(float(i))
    if type1 == "decimal":
        Nlist = []
        getcontext().prec = precision
        for i in range(1, n+1):
            Nlist.append(D(i))
    if type1 == "fraction":
        Nlist = []
        for i in range(1, n+1):
            Nlist.append(F(i))
    if type1 == "loadsofnumbers":
        Nlist = []
        for i in range(1, n+1):
            Nlist.append(float(i))        
    return Nlist

IntegerTime = []
FloatingTime = []
DecimalTime = []
FractionTime = []
LongNumberTime = []
Nlist = []
for i in range(1,10000,100):
    Nlist.append(i)
    IntegerTime.append(timeit.timeit(lambda: mysum(createlist(1000, "integer",2),"integer"),number=100))
for i in range(1,10000,100):
    Nlist.append(i)
    FloatingTime.append(timeit.timeit(lambda: mysum(createlist(2, "floating",2),"floating"),number=100))
for i in range(1,10000,100):
    Nlist.append(i)
    DecimalTime.append(timeit.timeit(lambda: mysum(createlist(2, "decimal",2),"decimal"),number=100))
for i in range(1,10000,100):
    Nlist.append(i)
    FractionTime.append(timeit.timeit(lambda: mysum(createlist(2, "fraction",2),"fraction"),number=100))
for i in range(1,10000,100):
    Nlist.append(i)
    LongNumberTime.append(timeit.timeit(lambda: mysum(createlist(2, "loadsofnumbers",2),"loadsofnumbers"),number=100))
    
plt.plot(IntegerTime,'ro',FloatingTime,'g^', DecimalTime, 'bo', FractionTime, 'y^', LongNumberTime, 'go')
plt.axis([0,100,0,0.1])
plt.show()

print mysum(createlist(100, "integer", 100))
print "integer time: ", IntegerTime
print "floating time: ",FloatingTime
print "decimal time: ",DecimalTime
print "fraction time: ",FractionTime
print "long number time:", LongNumberTime

print Nlist