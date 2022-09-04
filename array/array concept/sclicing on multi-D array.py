#slicing on multi-D array for using numpy.......
from numpy import *
a = array([[10,20,30],
           [40,50,60],
           [70,80,90]])
print(a)
print("new array")
#n = a[1:,0:2]
#n = a[0:3:2,0:3:2]
n = a[1:1:,2:1:]
print(n)