# Program make a simple calculator

first = int(input("enter first number: "))
operator = input("enter oprator (+,-,*,/,%): ")
second = int(input("enter second number: "))

if operator == "+":
    print(first + second)

elif operator == "-":
    print(first - second)

elif operator == "*":
    print(first * second)

elif operator == "/":
    print(first / second)

elif operator == "%":
    print(first % second)

else:
    print("invalid operator")