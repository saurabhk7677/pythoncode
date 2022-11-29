#decorator function.............................................
def decor(fun):
    def inner():
        print("Before enhancing function")
        fun()
        print("After enhancing function")
    return inner

def num():
    print("we will use the function")
    print("and will enhancing this in decorators")

result_fun = decor(num)
result_fun()
print()

#################################################################################

def decor(fun):
    def inner():
        print("Before enhancing function")
        fun()
        print("After enhancing function")
    return inner

@decor
def num():
    print("we will use the function")
    print("and will enhancing this in decorators")

num()
print()


######################################################################################

def decor(fun):
    def inner():
        a = fun()
        add = a + 5
        return add
    return inner
    
def num():
    return 10

result_fun = decor(num)
print(result_fun())