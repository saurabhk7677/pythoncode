#List of Tuples.......
a = [10, 20, (23,34)]
print(type(a))
print(id(a))
print("original list A:", a)
print()

#Accessing List of Tuple using for loop
n = len(a)
for i in range(n):
    if type(a[i]) is tuple:
        if len(a[i])>1:
            m = len(a[i])
            for j in range(m):
                print(i,j, a[i][j])
    else:
        print(i, a[i])




# 2nd example.....
a = [(10,20), (30,40)]
print('Original List A: ', a)
print(id(a))
print()


#Accessing List of Tuple using For Loop.....
n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i,j, a[i][j])
    print()
