
n  = int(input("Enter no of data : "))
l=[]

for i in range(n):
    a = int(input("Enter data : "))
    l.append(a)



# i.e 1 to n-1 times loop n-1 times
for k in range(1,n):   
    flag = 0
     # i.e 0 to n-k-1
    for i in range(0,n-1):  

        if(l[i]>l[i+1]):
            # swap
            l[i],l[i+1] = l[i+1],l[i]
            flag = 1

    if(flag == 0):
        break

for i in range(n):
    print(l[i])
