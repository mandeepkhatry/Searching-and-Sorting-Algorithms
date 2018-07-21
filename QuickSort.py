
n  = int(input("Enter no of data : "))
A=[]

for i in range(n):
    b = int(input("Enter data : "))
    A.append(b)


def QuickSort( A ,start ,end):

    #base condition
    if(start>=end):
        return
    
    pIndex  = Partition(A, start,end)
    
    QuickSort(A, start , pIndex-1)
    QuickSort(A, pIndex+1, end)


def Partition ( A, start ,end):
    pIndex = start

    pivot = A[end]

    # from start to end-1
    for i in range(start,end):
        if(A[i]<=pivot):
            A[i], A[pIndex] = A[pIndex] , A[i]
            pIndex = pIndex+1

    if(pivot == A[end]):print("Hello")
    
    A[pIndex] , A[end] = A[end], A[pIndex]

    return pIndex
        
QuickSort(A,0,n-1)

print(A)
