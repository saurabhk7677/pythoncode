a = [10, 20, 30, 40, 50]
b = a[:]
print("A:",a)
print("B:",b)
print()

print("Modifying of A")
a[1] = 99
print("A:",a)
print("B:",b)
print()

print("Modifying pf B")
b[2] = 'Apple'
print("A:",a)
print("B:",b)
print()


b = a[1:4]
print("A:",a)
print("B:",b)
