import sys
import timeit as time
import random

sys.setrecursionlimit(700000)

def mergeSort(forSorting):
    if len(forSorting)==1:
        return forSorting
    else:

        l = len(forSorting)
        n = int(l/2)
        arrayOne = mergeSort(forSorting[:n])
        arrayTwo = mergeSort(forSorting[n:])
        
        return merging(arrayOne,arrayTwo)


def merging(a,b):
    answer = []

    while len(a)>0 and len(b)>0:
        if (a[0]>b[0]):
            answer.append(b[0])
            b.pop(0)
        else:
            answer.append(a[0])
            a.pop(0)

    while len(a)>0:
        answer.append(a[0])
        a.pop(0)
    
    while len(b)>0:
        answer.append(b[0])
        b.pop(0)

    return answer

tiempos = []
largo = []
j=0
for f in range (1000,20001,950):
    nums = []
    for p in range (1,f+1):
        nums.append(random.randint(1,100000))
    largo.append(f)
    start_time = time.default_timer()
    mergeSort(nums)
    tiempos.append((time.default_timer()-start_time)*1000)
    print(tiempos[j])
    j = j+1

print(mergeSort([6,8,2,3,10,50,34,7,1,12]))
print(tiempos)
print(largo)