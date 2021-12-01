a=[101,102,103,104]
b=[2,3,4]
allitems=[]
i=0

for i in range(len(a)):
    allitems.append(a[i])

for j in range(len(b)):
    allitems.append(b[j])
    i+=1

for i in range(len(allitems)):
    print(allitems[i])
