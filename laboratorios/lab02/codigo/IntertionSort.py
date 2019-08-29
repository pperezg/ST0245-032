import timeit
import sys
import bisect

sys.setrecursionlimit(1000000)

def insertion_sort(list):
    for i in range(1, len(list)):
        value = list[i]
        j = i - 1
        while j >= 0:
            if value < list[j]:
                list[j + 1] = list[j]
                list[j] = value
                j -= 1
            else:
                break

a = []
tiempos = []
for f in range (10000,20001,500):
    b = []
    for n in range (1,f):
        b.append(n)
    a.append(f)
    start_time = timeit.default_timer()
    insertion_sort(b)
    tiempos.append((timeit.default_timer()-start_time)/1000)

print(a)
print(tiempos)