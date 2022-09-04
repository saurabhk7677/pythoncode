#where method.....
from numpy import *
a = array([100,200,300,400,500])
b = array([100,20,30,400,50])
result = where(a<b,a,b)          #(<,>,<=,>=,!=) we can use all relational operator
print(result)
print("*******************************")


#nonzero function......
from numpy import *
a = ([100,200,13,0,400,500,0])
result = nonzero(a)                 #print index number
print(result)
print("*******************************")



#aliasing method............
from numpy import *
a = array([10,20,30,40,50])
b = a
print(a)
print(b)
print()
a[2]=45
b[1]=90
print(a)
print(b)
print()
print("a",id(a))
print("b",id(b))
print("*********************************")



#view method.....
from numpy import *
a = array([10,20,30,40,50])
b = a.view()
a[1]=80
a[2]=300
print(a)
print(a)
print()
print("a",id(a))
print("b",id(b))
print("*********************************")



#copy method...........
from numpy import *
a = array([10,20,30,40,50])
b = copy(a)
a[1]=80
b[2]=300
print(a)
print(b)
print()
print("a",id(a))
print("b",id(b))