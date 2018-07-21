
n  = int(input("Enter no of data : "))
a=[]

for i in range(n):
    b = int(input("Enter data : "))
    a.append(b)


# 0 to n-2 loop
for k in range(0,n-1):
    minimum = k

    # i = k+1 to n-1
    for i in range(k+1,n):
        if (a[i] < a[minimum]):
            minimum = i

    #swap
    a[k] , a[minimum] = a[minimum] , a[k]

for i in range(n):
    print(a[i])
