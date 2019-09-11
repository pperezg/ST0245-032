import timeit
import sys
import random

sys.setrecursionlimit(10000000)

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

q = []
for w in range (1,2900):
    q.append(random.randint(1,100000))
j = len(q)
start_time = timeit.default_timer()
insertionSortRecursive(q,j)
print((timeit.default_timer()-start_time)*1000)

'''a = []
tiempos = []
for f in range (100,2001,95):
    b = []
    for n in range (1,f):
        b.append(n)
    a.append(f)
    j = len(b)
    start_time = timeit.default_timer()
    insertionSortRecursive(b,j)
    tiempos.append((timeit.default_timer()-start_time)*1000)

print(a)
print(tiempos)'''