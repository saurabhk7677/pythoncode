from numpy import *
a = ones((3,2),dtype=int)
print(a)
print()

#without index using for loop....
# for i in a:
#     for j in i:
#         print(j)
#     print()


#with index using for loop......
# n = len(a)
# for i in range(n):
#     for j in range(len(a[i])):
#         print("Index",i,j,"=",a[i][j])
#     print()


#without index using while loop....
# n = len(a)
# i = 0
# while (i<n):
#     j = 0
#     while (j<len(a[i])):
#         print(a[i][j])
#         j+=1
#     i+=1
#     print()




#with index using while loop....
n = len(a)
i = 0
while (i<n):
    j = 0
    while(j<len(a[i])):
        print("Index",i,j,"=",a[i][j])
        j+=1
    i+=1
    print()