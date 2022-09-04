#Memory Alloccation String...........

str1 = "geekyshows"
str2 = "geekyshows"
print(id(str1))
print(id(str2))
print()


############################################################


str3 = "geekyshows"
str4 = "geekyshows"
str5 = "python"
str6 = str5
print("str3=",id(str3))
print("str4=",id(str4))
print("str5=",id(str5))
print("str6=",id(str6))
print()


###########################################################################################


str7 = "hello world"
print(id(str7))
str7 = "python"
print(id(str7))