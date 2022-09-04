#function return another function............
def disp():
    print("disp function")

    def show():
        return "show function"
    return show

sk = disp()
print(sk())
print()



#function return another function.........
def disp(sh):
    print("disp function")
    return sh

def show():
    return "show function"

sk = disp(show())
print(sk)