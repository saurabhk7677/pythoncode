d = [{"id":1, "qty":5},{"id":2,"qty":3},{"id":3,"qty":4}]
# for j in range(len(d)):
#     i=0
#     while i<d[j]["qty"]:
#         print(d[j]["id"],end=" ")
#         i+=1

l = []
for i in d:
    l.extend(list(str(i["id"]) * i["qty"]))
    
print(l)




# l = [1,1,1,1,1,2,2,2,3,3,3,3]

# delete = 1
# l = [2,2,2,3,3,3,3]

# update
# id = 3 qty 10
# l = [2,2,2,3,3,3,3,3,3,3,3,3,3]

# dict convert
# [] = {}