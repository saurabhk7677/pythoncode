# from numpy import *
# a = array([[10,20,30,40],
#            [50,60,70,80]])
# print(a)
# print(type(a))
# print(a[0][0])
# print(a[0][1])
# print(a[0][2])
# print(a[0][3])
# print()
# print(a[1][0])
# print(a[1][1])
# print(a[1][2])
# print(a[1][3])
# print()
# a[0][3]=100
# print(a)
# print(id(a))
# print(id(a[0]))
# print(id(a[0][0]))
# print(id(a[1][3]))



#without index multi-array
# from numpy import*
# a = array([[10,20,30,40],
#            [50,60,70,80]])

# for i in a:
#     for j in i:
#         print(j)
#     print()

# n = len(a)
# i = 0
# while (i<n):
#     j=0
#     while(j<(len(a[i]))):
#         print(a[i][j])
#         j+=1
#     i+=1
#     print()





#withindex multi-d array...(for loop using)
# from numpy import*
# a = array([[10,20,30,40],
#            [50,60,70,80]])

# n = len(a)
# for i in range(n):
#     for j in range(len(a[i])):
#         print("index",j,"=",a[i][j])
#     print()


#with index multi-d array...(while loop using)
from numpy import *
a = array([[10,20,30,40],
           [50,60,70,80]])

n = len(a)
i = 0
while (i<n):
    j = 0
    while (j<(len(a[i]))):
        print("Index",j,"=",a[i][j])
        j+=1
    i+=1
    print()

