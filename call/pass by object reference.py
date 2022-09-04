# CALL / PASS BY OBJECT REFRENCE....

def val(x):
    x = 10
    print(x, id(x))

x = 15
val(x)
print(x, id(x))
print()

############################################################################


def val(lst):
    print("IFBA: ",lst,id(lst))
    lst.append(4)
    print("IFAA: ",lst,id(lst))

lst = [1,2,3]
print("BCF: ",lst,id(lst))
val(lst)
print("ACF: ",lst,id(lst))
print()

############################################################################


def val(lst):
    print("IFBA: ",lst,id(lst))
    lst = [11,22,33]
    print("IFAA: ",lst,id(lst))

lst = [1,2,3]
print("BCF: ",lst,id(lst))
val(lst)
print("ACF: ",lst,id(lst))