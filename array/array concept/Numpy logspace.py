#for loop using logspace numpy....
from numpy import *
a = logspace(1,3,5)
n = len(a)
for i in range(n):
    print("Index",i,"=",a[i])

print(id(a[2]))

print("*********************")
#while loop using logspace numpy....
from numpy import *
b = logspace(1,6,8)
n = len(b)
i = 0
while (i<n):
    print("Index",i,"=",b[i])
    i+=1

print(b[4])                                           
print(id(b[4]))
