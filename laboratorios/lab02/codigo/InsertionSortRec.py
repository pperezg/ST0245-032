import timeit
import sys
import bisect

sys.setrecursionlimit(1000000)

def insertionSortRecursive(arr,n):
    if n<=1: 
        return
    
    else:
        insertionSortRecursive(arr,n-1)

        last = arr[n-1] 
        j = n-2

        while (j>=0 and arr[j]>last): 
            arr[j+1] = arr[j] 
            j = j-1
    
        arr[j+1]=last 

a = []
tiempos = []
for f in range (2500,3501,50):
    b = []
    for n in range (1,f):
        b.append(n)
    a.append(f)
    j = len(b)
    start_time = timeit.default_timer()
    insertionSortRecursive(b,j)
    tiempos.append((timeit.default_timer()-start_time)*1000)

print(a)
print(tiempos)