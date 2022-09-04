#user input multi-d array......(using for loop)
# from numpy import *
# m = int(input("enter no of rows: "))
# n = int(input("enter no of columns: "))
# a = zeros((m,n),dtype=int)

# u = len(a)
# for i in range(u):
#     for j in range(len(a[i])):
#         x = int(input("enter element: "))
#         a[i][j] = x

# for i in range(u):
#     for j in range(len(a[i])):
#         print("Index",i,j,"=",a[i][j])
# print(a)





#user input multi-D array.....(using while loop)
from numpy import *
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
a = zeros((m,n),dtype=int)
u = len(a)
print(a)

i = 0
while (i<u):
    j = 0
    while (j<len(a[i])):
        x = int(input("Enter element: "))
        a[i][j] = x
        j+=1
    i+=1

u = len(a)
i = 0
while (i<u):
    j = 0
    while (j<len(a[i])):
        print("Index",i,j,"=",a[i][j])
        j+=1
    i+=1
print(a)
