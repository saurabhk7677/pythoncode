x = [[10,20,30],
     [40,50,60],
     [70,80,90],
     [11,22,33],
     [44,55,66],
     [77,88,99],
     [12,13,14]]

print("Original List")
print(x)

print("From 1st position to 4th position")
a = x[1:5]
print(a)
print()

print("from 0th position to last position")
b = x[0:]
print(b)
print()

print("from 0th position to 4th position")
c = x[:5]
print(c)
print()

print("last 4th list")
d = x[-4:]
print(d)
print()

print("from 0th position to 6th postion step size 2")
e = x[0:7:2]
print(e)
print()

print("last 5 lists with [-5-(-3)]=2")
f = x[-5:-3]
print(f)
print()

print("slice nested 2nd position , 0th position ")
m = x[2:3]
print(m)
g = [2:3][0]
print(g)
print()

print("slice 2nd list then extract elements")
h = x[2:3][0][0]
print(h)
i = x[2:3][0]
for el in i:
    print(el)
print()

print("last nested 4 lists then 1st position")
n = x[-4:]
print(n)
j = x[-4:][1]
print(j)

print("last nested 4 lists then 1st position then extract elements")
k = x[-4:][1][0]
print(k)
l = x[-4:][1]
for el in l:
    print(el)