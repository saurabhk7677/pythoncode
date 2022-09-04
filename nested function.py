#nested function........

def disp():
    def show():

        print("show function")
    print("disp function")

    show()
disp()


#nesting concatinated function.............
def disp():
    def show():

        return "show function"
    result = show() + " disp function"
    return result

a = disp()
print(a)



#with parameter nested function.......
def disp(st):
    def show():

        return "show function"
    result = show() + st + " disp funtion"
    return result

print(disp(" saurabh"))