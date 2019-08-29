import matplotlib.pyplot as plt 
import timeit
import sys

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
for f in range (20000,50001,10000):
    b = []
    for n in range (1,f):
        b.append(n)
    a.append(f)
    start_time = timeit.default_timer()
    insertion_sort(b)
    tiempos.append(timeit.default_timer()-start_time)

plt.plot(a,tiempos,'ro')
plt.axis([20000,50000,0,1])
plt.ylabel('tiempo en segundos')
plt.xlabel('largo del arreglo')
plt.show()