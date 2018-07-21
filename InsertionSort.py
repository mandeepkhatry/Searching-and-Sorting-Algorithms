
n  = int(input("Enter no of data : "))
a=[]

for i in range(n):
    b = int(input("Enter data : "))
    a.append(b)

# 1 to n-1 loop
for k in range(1,n):
    # k to 1 k--
    for i in range (k,0,-1):
        if(a[i]<a[i-1]):
            #swap
            a[i],a[i-1] = a[i-1] ,a[i]


for i in range(n):
    print(a[i])
