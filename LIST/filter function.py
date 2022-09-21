a = [10, 50, 60, 80, 90, 5, 45, 65]

def high_marks(n):
    if n>=60:
        return True

result = filter(high_marks,a)
print(result)
print(type(result))
print()


# Using list output......
b = [10, 50, 60, 80, 90, 5, 45, 65]

def high_marks(m):
    if m>=60:
        return True

result = list(filter(high_marks,a))
print(result)
print(type(result))
print()


# using lambda function.....
c = [10, 50, 60, 80, 90, 5, 45, 65]
result = list(filter(lambda n: n>=60 ,a))
print(result)
print()

####################################################################


m = [True, False, True, False, True, True]

result = list(filter(None,m))
print(result)
for z in result:
    print(z)