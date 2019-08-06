import matplotlib.pyplot as plt 
import timeit
import sys
def list_sum(num_List,count):
    if len(num_List) == count: # C1
        return 0
    else:
        return num_List[count] + list_sum(num_List, count + 1) # T(n) = T(n - 1) +C2

print(list_sum(num_List = [4, 5, 6, 7],count = 0))

sys.setrecursionlimit(30000)

a = []
tiempos = []
for n in range (1,5000):
    a.append(n)
    start_time = timeit.default_timer()
    list_sum(a,0)
    tiempos.append(timeit.default_timer()-start_time)

plt.plot(a,tiempos,'ro')
plt.axis([0,5000,0,0.2])
plt.ylabel('tiempo en segundos')
plt.xlabel('largo del arreglo')
plt.show()
