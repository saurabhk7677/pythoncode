#list data type

# a = [10, 33, -21, 34.32, "SUARABH"]

# print(len(a),a)
# a[0]=76
# a[1]=12
# a[2]=-34
# a[3]=89.234
# a[4]="KTM"
# print(type(a))
# print(id(a))
# print(a)
# print(id(a))



#set data type

a = {'saurabh', 'shubham', 'prakash', 'dignambar', 'dhanesh'}
b = {'java', 'prakash', 'python', 'shubham', 'c', 'cpp', '.net'}
c = {'.net', 'javascrip','shubham','react','dhanesh','cpp'}

print("a:", a)
print("b:",b)

#intersection function
# ism = a.intersection(b.intersection(c))
# print(ism)

# #union function
# um = a.union(b.union(c))
# print(um)

# #differnce function
df = a.difference(b.intersection(c))
print(df)

# df = b.difference(a)
# print(df)

# #issubset function
# df = a.issubset(b)
# print(df)

# df = b.issubset(a)
# print(df)

# #issuperset function
# df = a.issuperset(b)
# print(df)

# df = b.issuperset(a)
# print(df)

# #

