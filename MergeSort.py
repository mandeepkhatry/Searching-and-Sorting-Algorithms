
def MergeSort(A):
    n = len(A)

    if(n>1):
            

        mid = int(n/2)
        
        L = A[:mid]
        R = A[mid:]
        
        MergeSort(L)
        MergeSort(R)
        Merger(L,R,A)

def Merger(L,R,A):
        nL = len(L)
        nR = len(R)
        #initial 
        i , j , k = 0, 0, 0

        while((i < nL) and (j<nR)):
            if(L[i] < R[j]):
                A[k] = L[i]
                i = i+1
               

            else:
                A[k] = R[j]
                j = j+1
            
            k=k+1

        while(i < nL):
            A[k] = L[i]
            i=i+1
            k=k+1

        while(j < nR):
            A[k] = R[i]
            j=j+1
            k=k+1


n1  = int(input("Enter no of data : "))
A=[]

for i in range(n1):
    b = int(input("Enter data : "))
    A.append(b)

MergeSort(A)

print(A)


