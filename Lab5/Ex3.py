row = int(input("How many rows would you like to have in the multiplication table ( Choose between 1 and 15):"))

if row<16 and row>1:
    print("X", end=" ")
    for i in range(1, row + 1):
        print(i, end=" ")
    print()
    for i in range(1, row + 1):
        print(i, end=" ")
        for j in range(1, i+1):
            print(i * j, end=" ")
        print()
        
else:
    while row>15 or row<1:
        row = int(input("How many rows would you like to have in the multiplication table (Choose between 1 and 15):"))
    print("X", end=" ")
    for i in range(1, row + 1):
        print(i, end=" ")
    print()
    for i in range(1, row + 1):
        print(i, end=" ")
        for j in range(1, i+1):
            print(i * j, end=" ")
        print()
