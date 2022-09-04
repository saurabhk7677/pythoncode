#pass a function parameter..........
def disp(sk):
    print("disp function" + sk())

def show():
    return " show function"

disp(show)
print()


#################################

def disp(sk):
    return "disp function" + sk()

def show():
    return " show function"

result = disp(show)
print(result)