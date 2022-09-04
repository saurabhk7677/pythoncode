#getting input from users using for loop....

from array import *
stu_roll = array('i', [])
n = int(input("Enter number of elements: "))

for i in range(n):
    stu_roll.append(int(input("enter element: ")))

for i in range(len(stu_roll)):
    print(stu_roll[i])
print(stu_roll)


#getting input from users using while loop....

# from array import *
# stu_roll = array('i', [])
# n = int(input("Enter number of element: "))
# i = 0
# j = 0

# while (i<n):
#     stu_roll.append(int(input("Enter element: ")))
#     i+=1

# while (j<len(stu_roll)):
#     print(stu_roll[j])
#     j+=1




