# a = 10
# if a:
#     print("always true if statement")
# else:
#     print("control can never reach in else")


# wap given max no.

# a,b,c=int(input("enter number1 ")),int(input("enter number2 ")),int(input("enter number3 "))
# if a==b==c:
#     print("all are same")
# elif a>b:
#     if a>c:
#         print("A is max")
#     else:
#         print("B is max")
# elif b>c:
#     print("B is max")
# else:
#     print("C is max")



a,b,c=int(input("enter number1 ")),int(input("enter number2 ")),int(input("enter number3 "))
if a==b==c:
    print("all are same") 
elif a<b:
    if a<c:
        print("A is min")
    if a==b:
        print("A & B are same")
    else :
        print("B is min")
    if b==a:
        print("B & A are same")
elif b<c:
    print("B is min")
else:
    print("C is min")
if c==a:
    print("C & A are same")