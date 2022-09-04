#Array using insert function.......

# from array import *
# stu_roll = array('i',[101,102,103,104,105])
# n = len(stu_roll)
# i = 0
# while (i<n):
#     print(stu_roll[i])
#     i+=1

# print("Array After Insert")
# stu_roll.insert(2,106)
# stu_roll.insert(4,107)
# n = len(stu_roll)
# i = 0
# while (i<n):
#     print(stu_roll[i])
#     i+=1


#Array using pop function.....

# from array import *
# stu_roll = array('i',[101,102,103,104,105])
# j = stu_roll.pop()
# n = len(stu_roll)
# i = 0
# while (i<n):
#     print(stu_roll[i])
#     i+=1 
# print("This is a pop element: ",j)


#Array using  pop(n)"position number"

# from array import *
# stu_roll = array('i',[101,102,103,104,105])
# m = stu_roll.pop(1)
# n = len(stu_roll)
# i = 0
# while (i<n):
#     print(stu_roll[i])
#     i+=1
# print("This is a pop element ", m)



#Array using remove function.....

# from array import *
# stu_roll = array('i', [101,102,103,104,105])
# s = stu_roll.remove(103)
# n = len(stu_roll)
# i = 0
# while (i<n):
#     print(stu_roll[i])
#     i+=1


#Array using index function......

from array import *
# stu_roll = array('i',[101,102,103,104,105])
# n = len(stu_roll)
# i = 0

# while (i<n):
#     print("Index",i,"=",stu_roll[i])
#     i+=1

# for i in range(n):
#     print("Index", i,"=",stu_roll[i])


#Array using reverse function....
# from array import *
# stu_roll = array('i',[101,102,103,104,105])
# stu_roll.reverse()
# n = len (stu_roll)
# i = 0
# while (i<n):
#     print(stu_roll[i],end=" ")
#     i+=1

# for i in range(n):
#     print(stu_roll[i],end=" ")



#Array using extend() function......
# from array import *
# stu_roll = array('i',[101,102,103,104,105])
# ar = array('i',[106,107,107,108])
# print(stu_roll)
# print()
# stu_roll.extend(ar)
# n = len(stu_roll)
# i = 0
# while (i<n):
#     print(stu_roll[i],end=" ")
#     i+=1
# print()
# for i in range(n):
#     print(stu_roll[i],end=" ")


#Array using slicing method.......
from array import *
stu_roll = array('i',[101,102,103,104,105,106,107,108])
n = len(stu_roll)
for i in range(n):
    print(i,"=",stu_roll[i])
print()
a = stu_roll[1:5]
for i in a:
    print(i,end=" ")


