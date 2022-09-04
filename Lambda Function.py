#calling lambda function......
show = lambda x : print(x)
show(7)
print()

name = lambda user_name : print(user_name)
name('saurabh')
print()

add = lambda x,y : x + y
print(add(5,6))
print()


add_sub = lambda x,y : (x + y, x - y)
a,s  = add_sub(3,4)
print(a)
print(s)
print()


add = lambda x, y=10 : x + y
print(add(6))
print()


#nested lambda function...........
add = lambda x=10 : (lambda y : x + y)
a = add()
print(a)
print(a(20))
print()




#passing lambda function to another function.......
def show(a):
    print(a(8))

show(lambda x : x)
print()



#Returning lambda function.....

def add():
    y = 20
    return (lambda x : x + y)

a = add()
print(a(10))
