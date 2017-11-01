# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 22:35:28 2015

@author: louiscarnec
"""

from decimal import getcontext, Decimal as D
from fractions import Fraction as F
import timeit 
import matplotlib.pyplot as plt
import sympy

def theSum(mylist):
    s=0
    for i in mylist: 
        s += i
    return s

#def theSum(alist, start=0, stop=0):
#    result=0
#    while start <= stop:
#        result = result + start
#        start += 1
#    return result
#    
#def theSum(start=0, stop=0):
#    result=0
#    for i in n:    
#        while start <= stop:
#            result = result + start
#            start += 1
#    return result
    
def createIntlist(n):
    Nlist = []
    for i in range(1, n+1, 10):
        Nlist.append(i)
    return Nlist
    
print createIntlist(1000)
print theSum(createIntlist(10000000000))
   

runtime = timeit.timeit(lambda:theSum(Nlist), number=100)
print runtime

































