# a = [10, 20, 30, [50,60]]
# n = len(a)

# for i in range(n):
#    if type(a[i]) is list:
#         if len(a[i])>1:
#             m=len(a[i])
#             for j in range(m):
#                 print(i,j, a[i][j])

#     else:
#         print(i,a[i])


###################################################################

b = [[10,20,30],[40,50,60]]

for r in b:
    for c in r:
        print(c)
    print()


######################################################################

c = [[10,20,30],[40,50,60]]

n = len(c)
for i in range(n):
    for j in range(len(c[i])):
        print(i,j,c[i][j])
    print()










        