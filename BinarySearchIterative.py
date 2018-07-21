def BinarySearch(A,n,x):
    start = 0
    end = n-1

    while(start<=end):
        mid = int((start+end)/2)

        if(x == A[mid]):
            print("Found ")
            return x
        elif(x<A[mid]):
            end = mid-1
        else:
            start = mid+1
    print("Not found")
    return -1

n  = int(input("Enter no of data : "))
A=[]

for i in range(n):
    b = int(input("Enter data : "))
    A.append(b)

b = int(input("Enter data to be searched : "))

BinarySearch(A,n,b)
