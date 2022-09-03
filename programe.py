#person is eligible to vote or not.
age = int(input("enter the age: "))
if age>=18:
	print("you are eligible to vote")
else:
	yrs = 18 -age
	print("you have to wait for another " + str(yrs) + " years to cast your vote")



#determine the character entered by the user.
# char = input("press any key: ")
# if char.isalpha():
# 	print("the user has entered character")
# if char.isdigit():
# 	print("the user has entered digit")
# if char.isspace():
# 	print("the user has entered space character")



#given number is even or odd.
num = int(input("enter the number: "))
if num%2==0:
	print(num,"is even")
else:
	print(num,"is odd")



#year is a leep year or not.
# year = int(input("enter any year: "))
# if year%4==0 and year %100!=0 or year%400==0:
# 	print("leap year")
# else:
# 	print("not a leap year")

