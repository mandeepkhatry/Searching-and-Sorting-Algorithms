def BinarySearch(A,start,end,x):
        mid  = int((start+end)/2)
        if(start>end):
            print(" Not Found ")
            return -1
        if(x == A[mid]):
            print("Found ")
            return x
        elif(x<A[mid]):
            BinarySearch(A, start, mid-1,x)

        else:
            BinarySearch(A,mid+1,end,x)


n  = int(input("Enter no of data : "))
A=[]

for i in range(n):
    b = int(input("Enter data : "))
    A.append(b)

b = int(input("Enter data to be searched : "))
        
BinarySearch(A,0,n-1,b)
