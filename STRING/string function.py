# upper() =  convert all string upper case.
# name = "geekyshows"
# str1 = name.upper()
# print(name)
# print(str1)
# print()

# # lower()- conver all string lower case.
# name = "GEEKYSHOWS"
# str1 = name.lower()
# print(name)
# print(str1)
# print()

# # swapcase() - convert string lower to upper and upper to lower.
# name = "geekyshows"
# str1 = name.swapcase()
# print(name)
# print(str1)
# print()

# name = "GEEKYSHOWS"
# str1 = name.swapcase()
# print(name)
# print(str1)
# print()

# title() - convert string into a title format.
# name = "hello how are you?"
# str1 = name.title()
# print(name)
# print(str1)

######################################################################################################################################################################

# isupper()- string is uppercase or not.
# name = "GEEKYSHOWS"
# str1 = name.isupper()
# print(name)
# print(str1)
# print()

# name = "gEEKYSHOWS"
# str1 = name.isupper()
# print(name)
# print(str1)
# print()

# # islower()- string is lowercase or not.
# name = "geekyshows"
# str1 = name.islower()
# print(name)
# print(str1)
# print()

# name = "Geekyshows"
# str1 = name.islower()
# print(name)
# print(str1)
# print()

# # istile() - this string title format or not.
# name = "Hello How Are You"
# str1 = name.istitle()
# print(name)
# print(str1)
# print()

# name = "hello how are you"
# str1 = name.istitle()
# print(name)
# print(str1)
# print()

#########################################################################################################################################################################

# isdigit()- returns only numeric digits (0 to 9)
# name = "77776879"
# print(name.isdigit())
# print()

# name = "65324584sksksk"
# print(name.isdigit())
# print()

# # isalpha() - returns only characters (A to Z and a to z)
# name = "GeekyShows"
# print(name.isalpha())
# print()

# name = "GeekyShows7677"
# print(name.isalpha())
# print()

#isalnum() - returns string and charcter all types.
# name = "Geekyshows325"
# print(name.isalnum())
# print()

# name = "768484"
# print(name.isalnum())
# print()

# name = "768484@!$%"
# print(name.isalnum())
# print()

# isspace() - return only string space.
# name = " "
# print(name.isspace())
# print()

# name = ""
# print(name.isspace())
# print()

# name = " saurabh "
# print(name.isspace())
# print()

######################################################################################################################################################################

# lstrip() - remove left space.
# name = "      Geekyshows"
# str1 = name.lstrip()
# print(name)
# print(str1)
# print()

# #rstrip() - remove right space.
# name = "      Geekyshows     "
# str1 = name.rstrip()
# print(name)
# print(str1)
# print()


# # strip() -  remove space both side.
# name = "      Geekyshows        "
# str1 = name.strip()
# print(name)
# print(str1)
# print()

######################################################################################################################################################################

# replace() - replace sub string into a another string.
# name = "Geekyshows"
# old = "Geeky"
# new = "New"
# str1 = name.replace(old,new)
# print(name)
# print(str1)
# print()

# name = "saurabhkadam"
# str1 = name.replace('saurabh','ganesh')
# print(name)
# print(str1)
# print()

# split() - split/break a string into pieces. return into list.
# name = "Hello_how_are_you"
# str1 = name.split('_')
# print(name)
# print(str1)
# print()

# name = "Hello how are ou"
# str2 = name.split(' ')
# print(name)
# print(str2)
# print()

# join() - join string into a one string.
# name = ('hello', 'how', 'are', 'you')
# str1 = '_'.join(name)
# print(name)
# print(str1)
# print()

# name = ('hello', 'how', 'are', 'you')
# str1 = ' '.join(name)
# print(name)
# print(str1)
# print()

######################################################################################################################################################################

# startswith() - string start with substring or not.
# name = "Hi how are you"
# str1 = name.startswith('Hi')
# print(str1)
# print()

# name = "Hi how are you"
# str1 = name.startswith('bye')
# print(str1)
# print()

# endswith() - string ends with substring or not.
# name = "Hi how are you"
# str1 = name.endswith('you')
# print(str1)
# print()

# name = "Hi how are you"
# str1 = name.endswith('bye')
# print(str1)
# print()

name = "Thank you Goodbye"
str1 = name.endswith('bye')
print(str1)