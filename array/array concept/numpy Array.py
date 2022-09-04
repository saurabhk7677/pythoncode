from numpy import *
stu_roll = array([101,102,103,104,105])
print(stu_roll)
print(stu_roll.dtype)
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])
stu_roll[3]=110
print(stu_roll)

#for loop using all element aceess...
for i in stu_roll:
    print(i)

print()

#while loop using all element access....
n = len(stu_roll)
i=0
while (i<n):
    print(stu_roll[i])
    i+=1

#for loop with index accessing element....
n = len(stu_roll)
for i in range(n):
    print("index",i,"=",stu_roll[i])

print()
#while loop with index accessing element....
j = 0
while (j<n):
    print("index",j,"=",stu_roll[j])
    j+=1

