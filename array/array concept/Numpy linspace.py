from numpy import *
a = linspace(1,9)
print(a)

n = len(a)
for i in range(n):
    print(a[i])

for j in range(n):
    print("Index",j,"=",a[j])

print("print while loop")

i = 0
while (i<n):
    print(a[i])
    i+=1

print("**********************")

m = 0
while (m<n):
    print("Index",m,"=",a[m])
    m+=1

print(a[37])
print(a[24])
