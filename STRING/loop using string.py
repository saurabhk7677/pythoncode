#for loop using string access...

str = "GeekyShows"
for c in str:
    print(c)
print()

#for loop with index usinge string access...

str1 = "Saurabh"
for i in range(len(str1)):
    print(str1[i])
print()


#while loop using string access.....

str2 = "Hello world"
i = 0
while (i<len(str2)):
    print(str2[i])
    i+=1
print()


#user input type string using for loop.......
x = input("Enter string: ")
for i in range(len(x)):
    print(x[i],end=" ")


#user input type string using while loop.......
x = input("Enter string: ")
i = 0
while (i<len(x)):
    print(x[i],end=" ")
    i+=1