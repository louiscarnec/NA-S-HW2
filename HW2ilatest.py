# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 21:06:27 2015

@author: josep_000
"""

from numpy import *

x = 1.0 + (0.001 - 1.0)
y = (1.0 + 0.001) - 1.0
print x, y, x==y
print "%.16f %.16f" % (x,y)

z = np.float32(0.1)
print "%.31f" %(z)

# Associativity of +
#If the result of an arithmetic operation is an integer outside this range then 
# an integer overflow occurs.
k = (np.float32(0.2) + np.float32(0.2)) + np.float32(1.0)
j = np.float32(0.2) + (np.float32(0.2) + np.float32(1.0))
print k,j,k==j
print "%.32f %.32f" %(k,j)

#Commutativity of +
#a+b = b+a
x = np.float64(0.1) + np.float64(0.2) + np.float64(0.3)
y =  np.float64(0.3) + np.float64(0.2) + np.float64(0.1)
print x,y,x==y
print "%.60f %.60f" % (x,y)

#-a is the additive inverse of a
#a + (a) = 0
x = 1.0/3.0
y = 1/3
xminusy = x - y
print xminusy
print x,y,x==y
print "%.60f %.60f" % (x,y)

#a + (a) = 0
x = 1.0/3.0
xminusx = round(x,3) + (-x)
print xminusx

# Associativity of Multiplication
k = (np.float32(math.pi) * np.float32(1.0)) * np.float32(1.0)
j = np.float64(math.pi) * (np.float64(1.0) * np.float64(1.0))
print k,j,k==j
print "%.64f %.64f" %(k,j)

# Left Distributivity
x = np.float16(1.0) * (np.float32(0.1) + np.float64(0.2))
y = (1.0 * 0.1) + (1.0 * 0.2)
print x,y,x==y
print "%.60f %.60f" % (x,y)

# Right Distributivity
x = (np.float32(0.1) + np.float64(0.2)) * np.float16(1.0) 
y = (1.0 * 0.1) + (1.0 * 0.2)
print x,y,x==y
print "%.60f %.60f" % (x,y)
















