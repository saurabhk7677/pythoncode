dict={}
dict["Name"]=["Prakash","Shubham","Saurabh"]
dict["Number"]=[10,20,30]


# print(dict)
# print(dict["Name"])
# print(type(dict["Name"]))
# print(dict["Number"])
# print(type(dict["Number"]))
# print(dict["Name"][0])
# print(dict["Name"][0][0])
# print(dict["Name"][0][6])
# print(dict["Name"][1])
# print(dict["Name"][1][0])
# print(dict["Name"][1][6])
# print(dict["Name"][2])
# print(dict["Name"][2][0])
# print(dict["Name"][2][6])
# print(dict["Name"]+dict["Number"])

a = dict["Name"]+dict["Number"]
# print(a)
# b = dict["Name"].extend(dict["Number"])
# print("list=",b)

tup  = tuple(a)
print(tup)