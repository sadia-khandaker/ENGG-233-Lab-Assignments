import random
def main():
    n=5  
    m=8
    array1=[]
    array2=[]
        
    for i in range(n):
        array1.append(random.randint(0,50))
        
    for i in range(m):
        array2.append(random.randint(0,50))

    array1=sorted(array1)
    array2=sorted(array2)

    print("Array 1 after sorting it:",array1)
    print("Array 2 after sorting it:",array2)
        
    array3=[]

    placement_of_array1=0
    placement_of_array2=0

    while(placement_of_array1<n and placement_of_array2<m):
        if(array1[placement_of_array1]<array2[placement_of_array2]):
            array3.append(array1[placement_of_array1])
            placement_of_array1+=1
        else:
            array3.append(array2[placement_of_array2])
            placement_of_array2+=1

    while(placement_of_array1<n):
        array3.append(array1[placement_of_array1])
        placement_of_array1+=1

    while(placement_of_array2<n):
        array3.append(array2[placement_of_array2])
        placement_of_array2+=1

    print("Merged array:",array3)
    
if __name__=="__main__":
    main()