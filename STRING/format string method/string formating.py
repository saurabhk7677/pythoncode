print("{:8s}".format("Geek"))
print("{:<8}".format("Geek"))
print("{:*<8}".format("Geek"))
print("{:>8}".format("Geek"))
print("{:*>8}".format("Geek"))
print("{:^8s}".format("Geek"))
print("{:*^8s}".format("Geek"))

print()



###################################################################3


print("{:.3s}".format("Geekshows"))
print("{:8.3s}".format("Geekshows"))
print("{:<8.3s}".format("Geekshows"))
print("{:*<8.3s}".format("Geekshows"))
print("{:>8.3s}".format("Geekshows"))
print("{:*>8.3s}".format("Geekshows"))
print("{:^8.3s}".format("Geekshows"))
print("{:*^8.3s}".format("Geekshows"))



#######################################################################


print("{:,}".format(1234567890))
print("{:_}".format(1234567890))

print()

######################################################################

# variable using .formating method..

name = "Rahul"
age = 62
print("My name is {} and age is {}".format(name,age))
print()


a = 50
b = 3
print("{:.2%}".format(a/b))
print()



##########################################

# accesing argument items........

value = (10, 20)
print("{0[0]} {0[1]}".format(value))
print()


data1 = {'Rahul': 2000, 'Sonal': 3000}
print("{d[Rahul]} {d[Sonal]}".format(d=data1))
print("{Rahul} {Sonal}".format(**data1))


