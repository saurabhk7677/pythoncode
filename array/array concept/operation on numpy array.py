#arithmatic operation with numpy.......
from numpy import *
a = array([100,200,300,400,500])
b = array([100,20,30,400,50])
z = [a]+[b]
print([z])
print(any(z))
print(all(z))
c = a+5
d = b-5
e = a+b
f = a/b
g = a*b
h = a%b
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
for i in e:
    print(i)

i=0
n=len(a+b)
while (i<n):
    print(a+b[i])
    i+=1
print("*******************************************")
print()

#Relational operation with numpy.......
from numpy import *
a = array([100,200,300,400,500])
b = array([100,20,30,400,50])
c = a==b
d = a<b
e = a>b
f = a<=b
g = a>=b
h = a!=b
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
n=len(a+b)
i=0
while (i<n):
    print("Index",i,"=",a[i])
    print("Index",i,"=",b[i])
    print("Index",i,"=",a+b[i])
    i+=1