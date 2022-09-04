#Global keyword..........
a = 50

def show():
    a = 10
    print("A: ",a)

show()
print("A: ",a)
print()


i = 0

def show():
    global i 
    i = i + 1
    print("A :",i)

show()
print("A :",i)
print()



i = 0

def myfun():
    global i
    while (i<5):
        i+=1
        print("Local variable A:",i)

myfun()
print("Gobal variable A:",i)
print()

#Globals () function.......

a = 100

def show():
    a = 30
    print("Local variable A: ",a)

show()
print("Global variable A: ",a)
print()


a = 40

def myfun():
    a = 70
    print("Local variable A: ",a)
    x = globals()['a']
    print("x :",x)

myfun()
print("Global variable A: ",a)
print()



#Recursion.......

def myfun():
    print("saurabh")
    myfun()

myfun()
print()



i = 0

def myfun():
    global i
    i = i + 1
    print("My function: ",i)
    myfun()

myfun()