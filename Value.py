# print("I Love {0} and {1}".format('Apple','Mango'))



# for i in range(4):
#     for j in range(4):
#         print("*", end=' ')
#     print()



s = 'hello'
x = [i for i in s]
print(x)


def generate_list():
    lst = list()
    for i in range(1,11):
        lst.append((i,i**2,i**3))
    return lst

l = generate_list()
print(l)