from numpy import *
a = zeros((3,2))
# print(a)
# print()

#without index multi-d array using for loop......
# for i in a:
#     for j in i:
#         print(j)
#     print()
# print()



#with index using for loop......
# n = len(a)
# for i in range(n):
#     for j in range(len(a[i])):
#         print("Index",i,j,"=",a[i][j])
#     print()
#print("*********rest of code**********")


#without index using for loop......
# n = len(a)
# i = 0
# while (i<n):
#     j = 0
#     while (j<(len(a[i]))):
#         print(a[i][j])
#         j+=1
#     i+=1
#     print()



with  index using whhile loop....
n = len(a)
i = 0
while (i<n):
    j = 0
    while(j<(len(a[i]))):
        print("index",i,j,"=",a[i][j])
        j+=1
    i+=1
    print()