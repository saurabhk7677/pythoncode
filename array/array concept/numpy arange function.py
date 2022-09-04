#for loop using arange function with numpy.........
from numpy import *
a = arange(1,10,2,dtype=int)
n = len(a)
for i in range(n):
    print("Index",i,"=",a[i])
print("*********************************")


#while loop using arange function with numpy.........
from numpy import *
a = arange(1,10,2,dtype=int)
n = len(a)
i = 0
while(i<n):
    print("Index",i,"=",a[i])
    i+=1
print("********************************")