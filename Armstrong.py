# To check if the number is an armstrong number or not

#take input from the user
num = int(input("enter number :"))
sum = 0     #Initiltion sum
temp = num   #find the sum of the cube of each digit
while temp > 0 :
    digit = temp % 10
    sum += digit ** 3    #sum=sum + digit * digit * digitS
    temp //= 10          #temp=temp // 10
if num == sum:           #display the result
    print(num,"is an armstrng number because sum=num",)
else:
     print(num,"is not an armstrng number because sum!=num",)



#153
#1 * 1 * 1 = 1
#5 * 5 * 5 = 125
#3 * 3 * 3 = 27
#153
#num = sum (153=153) o/p is valid


print("Hello shubham")