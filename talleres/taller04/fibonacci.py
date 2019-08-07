import matplotlib.pyplot as plt 
import timeit
import sys

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
a = []
tiempos = []
for f in range (1,41):
    a.append(f)
    start_time = timeit.default_timer()
    fibonacci(f)
    tiempos.append(timeit.default_timer()-start_time)
    
sys.setrecursionlimit(3000)

plt.plot(a,tiempos,'ro')
plt.axis([0,40,0,2])
plt.ylabel('tiempo en segundos')
plt.xlabel('largo del arreglo')
plt.show()