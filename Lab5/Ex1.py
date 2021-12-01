def fibonacci_number():
    n = 0
    while n < 3:
        n = int(input("Enter a positive integer number greater than or equal to 3: "))
    n0 = 0
    n1 = 1

    print(n)
    while n1 <= n:
        print(n1, end=' ')
        n0, n1 = n1, n0 + n1
    print()

fibonacci_number()