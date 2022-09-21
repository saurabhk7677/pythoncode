# Passing list to function..........

def show(n):
    print(n)
    for i in n:
        print(i)
lst = [10, 20, 30, 'saurabh']
show(lst)
print()





# Passing and returning list.....

def show(m):
    print(m)
    for i in m:
        print(i)
    return m
lst = [10, 20, 30, 'saurabh']
new_list = show(lst)
print(new_list)
print()



# List function.....

a = list("Geekyshows")
print(a)
print()


a = list(range(0,5))
print(a)