# string in for loop.
st = "saurabh"
for i in st:
    print(i)


# 2nd example in string.
st = "saurabh"
a = len(st)
for i in range(a):
    print(i,"=",st[i])


#for loop with else.
str = "saurabh"
for i in str:
    print(i)
else:
    print("else part")



#range in for loop.
a = range(5)
for i in a:
    print(i)


#2nd example in range
a = range(1,5)
for i in a:
    print(i)


#3rd example in range.
a = range(1,10,2)
for i in a:
    print(i)



#nested for loop.
for i in range(2):
    print("outer loop",i)
    for j in range(3):
        print("inner loop",j)
else:
    print("for loop end")