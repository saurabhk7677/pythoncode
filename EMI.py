loan_amount = int(input("loan amount "))
duration_year = int(input("enter total time "))
interest = int(input("enter rate of interest "))
downpayment = int(input("enter downpayment "))
amount = loan_amount - downpayment
simple_interest = (amount * duration_year * interest) / 100
emi = (amount + simple_interest) / (duration_year * 12)
print("your equated monthly instalment is ",emi)
