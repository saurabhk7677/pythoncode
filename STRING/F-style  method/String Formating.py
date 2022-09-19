name = "Geek"

print(f"{name}")
print(f"{name:s}")
print(f"{name:8s}")
print(f"{name:<8s}")
print(f"{name:*<8}")
print(f"{name:>8}")
print(f"{name:*>8}")
print(f"{name:^8s}")
print(f"{name:*^8s}")
print()


#############################################################


name = "GeekyShows"

print(f"{name:.3s}")
print(f"{name:8.3s}")
print(f"{name:<8.3s}")
print(f"{name:*<8.3s}")
print(f"{name:>8.3s}")
print(f"{name:*>8.3s}")
print(f"{name:^8.3s}")
print(f"{name:*^8.3s}")
print()


#########################################################################

# commas(,) and undescore(_) using formating.....

price = 1234567890
print(f"{price:,}")
print(f"{price:_}")
print()

###########################################################################

# variable using formating.....

name = "Rahul"
age = 62
print(f"My name is {name} and age is {age}")
print()

#################################################################################

print(f"{10 * 8}")
print()

#####################################################################################

a = 50
b = 3
print(f"{a/b:2%}")
print()

#########################################################################################
value = (10, 20)
print(f"{value[0]} {value[1]}")
print()

###########################################################################################

data = {'Rahul':2000, 'Sonam':3000}
print(f"{data['Rahul']:d} {data['Sonam']:d}")
print()

############################################################################################

name = "GeekyShows"
print(f"{name.upper()}")
print()

###########################################################################################

print(f"{{10}}")
print()

#############################################################################################

from datetime import datetime
today = datetime(2019,10,5)
print(f"{today}")