#without parameter function.............
def disp():
    name = "GeekyShows"
    print("welcome to",name)
disp()


#with parameter function.............
def add(y):
    x = 10.2334
    print(x + y)
    print(f"formatted output (x+y:5.2f)")
add(20)


#without parameter function............
def add():
    x = 10
    y = 20
    c = x + y 
    return c
sum = add()
print(sum)



#with parameter function...........
def add(y):
    x = 10
    return x + y
sum = add(20)
print(sum)



#with parameter function.......
def add(y):
    x = 10
    c = x + y
    d = y - x
    return c,d
sum , sub = add(20)
print(sum)
print(sub)



def welcome_user (name):
    print("welcome {}".format(name))
welcome_user('saurabh')


def welcome_user(name, country):
    print("welcome {}".format(name))
    print("your country is {}".format(country))

welcome_user(country='india',name='xyz')


def welcome_user(*name):
    for user_name in name:
        print("welcome {}".format(user_name))

welcome_user('shubham','saurabh','abhi','praksh','diganmbar','dhanesh')
