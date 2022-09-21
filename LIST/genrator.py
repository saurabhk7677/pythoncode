def disp(a,b):
    yield a
    yield b
result = disp(10,20)
print(result)
print(next(result))
print(next(result))
print()



###########################

def show(a,b):
    while a<=b:
        yield a
        a+=1

result = show(1,5)
print(result)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))