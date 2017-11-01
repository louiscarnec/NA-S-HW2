# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 02:24:35 2015

@author: josep_000
"""

from decimal import Decimal as D
from decimal import *

def formula(stop, z = ""):
    mylist = [4.0,4.25]
    mylist1 = [4.0,4.25]
    mylist2 = [4.0,4.25]
    mylist3 = [4.0,4.25]

    x0 = 4.0
    x1 = 4.25
    i = 0 
    if z == "%.1f":
        while i <= stop:
            xn = 108.0 - (815.0/x1)-(1500.0/(x0*x1))
            i = i+1
            x0=x1
            x1 = xn
            xn = ("%.1f" % xn)
            mylist.append(xn)
        return mylist
    if z == "%.5f":
        while i <= stop:
            xn = 108.0 - (815.0/x1)-(1500.0/(x0*x1))
            i = i+1
            x0=x1
            x1 = xn
            xn = ("%.5f" % xn)
            mylist1.append(xn)
        return mylist1
    if z == "%.10f":
        while i <= stop:
            xn = 108.0 - (815.0/x1)-(1500.0/(x0*x1))
            i = i+1
            x0=x1
            x1 = xn
            xn = ("%.10f" % xn)
            mylist2.append(xn)
        return mylist2
    if z == "%.100f":
        while i <= stop:
            xn = 108.0 - (815.0/x1)-(1500.0/(x0*x1))
            i = i+1
            x0=x1
            x1 = xn
            xn = ("%.100f" % xn)
            mylist3.append(xn)
        return mylist3
    
    
def formula1(stop, z = "1"):
    myList = [4,4.25]
    myList1 = [D(4),D(4.25)]
    myList2 = [D(4),D(4.25)]
    myList3 = [D(4),D(4.25)]
    x0 = D(4.0)
    x1 = D(4.25)
    i=0
    if "1":
        while i <= stop:
            xn = D(108) - (D(815.0)/x1)-(D(1500.0)/(x0*x1))
            i = i+1
            getcontext().prec = 1
            x0=x1
            x1 = xn
            myList.append(xn)
        return myList
    if "5":
        while i <= stop:
            xn = D(108.0) - (D(815.0)/x1)-(D(1500.0)/(x0*x1))
            i = i+1
            getcontext().prec = 5
            x0=x1
            x1 = xn
            myList1.append(xn)
        return myList1
    if "10":
        while i <= stop:
            xn = D(108.0) - (D(815.0)/x1)-(D(1500.0)/(x0*x1))
            i = i+1
            getcontext().prec = 10
            x0=x1
            x1 = xn
            myList2.append(xn)
        return myList2
    if "100":
        while i <= stop:
            xn = D(108.0) - (D(815.0)/x1)-(D(1500.0)/(x0*x1))
            i = i+1
            getcontext().prec = 10
            x0=x1
            x1 = xn
            myList3.append(xn)
        return myList3

a = formula(30,"%.1f")
a1 = formula(30,"%.5f")
a2 = formula(30,"%.10f")
a3 = formula(30,"%.100f")


print(a)
#print a1
#print a2
#print a3
#
b = formula1(30,"1")
b1 = formula1(30,"5")
#b2 = formula1(30,"10")
#b3 = formula1(30,"100")
#
print(b)
print(b1)
#print b2
#print b3
#
#fig = plt.figure()
#plt.plot(a, 'ro', a1, 'go', a2, 'bo',a3, 'y^',linestyle='-')
#plt.axis([0,35,-210,200])
#plt.xlabel('xn Approximations')
#plt.ylabel('xn')
#plt.title('')
#plt.show() 
#
#fig = plt.figure()
#plt.plot(b, 'ro', b1, 'go', b2, 'bo',b3,'y^',linestyle='-')
#plt.axis([0,35,-210,200])
#plt.xlabel('xn Approximations')
#plt.ylabel('xn')
#plt.title('')
#plt.show() 
#
#fig = plt.figure()
#plt.plot(a, 'ro', a1, 'go', a2, 'bo',a3, 'y^',b, 'r^', b1, 'g^', b2, 'b^',b3, 'yo',marker='o', linestyle='-')
#plt.axis([0,35,-210,200])
#plt.xlabel('xn Approximations')
#plt.ylabel('xn')
#plt.title('')
#plt.show() 
