x = [101, 102, 103, 104, 105, 106, 107]
print("Original list")

n = len(x)
for i in range(n):
    print(i, "=", x[i])
print()

print("from 1st position to 4th position")
a = x[1:5]
for i in a:
    print(i)
print()

print("from 0th position to last position")
b = x[0:]
for i in b:
    print(i)
print()

print("from 0th position to 4th position")
c = x[:5]
for i in c:
    print(i)
print()

print("last 4 elements")
d = x[-4:]
for i in d:
    print(i)
print()

print("0th position to 6th position with difference of 2")
e = x[0:7:2]
for i in e:
    print(i)
print()

print("Last 5 elements with [-5-(-3)] = 2 elements twards right")
f = x[-5:-3]
for i in f:
    print(i)
print()

############################################################################################

x = [55,89, 5, 45, 98, 12, 6, 34, 86, 34]
print("Original list")
n = len(x)

for i in range(n):
    print(i, "=", x[i])
print()

print("from 0thposition to 5th position  stride 2")
g = x[0:6:2]
for i in g:
    print(i)