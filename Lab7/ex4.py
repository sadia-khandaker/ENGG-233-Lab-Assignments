n=int(input("Enter a number: "))
matrix=[[0 for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        if (i+j)%2==0:
            matrix[i][j]=0
        else:
            matrix[i][j]=1
for i in range(n):
    for j in range(n):
        print(matrix[i][j],'',end=" ")
    print("\n")