sum_of_digits=0 
number=int(input("Enter positive integer number "))

while(number<0):
    print("Enter positive integer number")
    number=int(input())

while(number>0):
    sum_of_digits+=number%10 
    number=number//10  


print("Sum of digits for the input is: " ,sum_of_digits)

