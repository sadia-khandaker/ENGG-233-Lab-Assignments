counter = 0     
sum_of_odds = 0     
num_of_odds = 0    

n = int(input("Enter a positive integer : "))

while counter < n-1:
    counter += 1


    if counter % 2 != 0:

     print(counter)
     sum_of_odds += counter
     num_of_odds += 1



print("Sum of odds : ",sum_of_odds)

print("Average of odds :", sum_of_odds/num_of_odds)