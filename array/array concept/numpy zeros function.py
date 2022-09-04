#for loop using zeros function with numpy.........
from numpy import *
a = zeros(5,dtype=int)
n = len(a)
for i in range(n):
    print("Index",i,"=",a[i])
print("****************************")



#while loop using zeros function with numpy........
from numpy import *
a = zeros(5,dtype=int)
n = len(a)
i = 0
while (i<n):
    print("Index",i,"=",a[i])
    i+=1