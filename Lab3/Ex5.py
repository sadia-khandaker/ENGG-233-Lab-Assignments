number = str(input("Enter the 6 digit number:"))

firstdigit = int(number[0])

print ("The digits that are divisible by ",firstdigit," are ",end="" )


for i in range(1,len(number)):
    if int(number[i]) % firstdigit == 0 :
        print(number[i], end=" ")