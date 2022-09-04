#for loop using 1d array user input.......
from numpy import *
n = int(input("Enter number of element: "))
a = zeros(n,dtype=int)

for i in range(len(a)):
    x = int(input("Enter element: "))
    a[i] = x

for i in range(len(a)):
    print(a[i])

print(a)

print(type(a))
print()




#while loop using 1d array user input.......
# from numpy import *
# n = int(input("Enetr number of element: "))
# a = zeros(n,dtype=int)

# u = len(a)
# i = 0 
# j = 0

# while (i<u):
#     x = int(input("Enter element: "))
#     a[i]=x
#     i+=1

# while (j<u):
#     print(a[j])
#     j+=1

# print(type(a))