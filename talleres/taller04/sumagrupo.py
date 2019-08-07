import matplotlib.pyplot as plt 
import timeit
import sys
def Suma_grupo(start, nums, target):
    if start >= len(nums):
        if target == 0:
            return True
        else:
            return False
    return Suma_grupo(start + 1, nums, target) or Suma_grupo(start+1, nums, target-nums[start])

print(Suma_grupo(0,[2, 4, 8],10))

sys.setrecursionlimit(30000)

a = []
tiempos = []
for n in range (1,21):
    a.append(n)
    start_time = timeit.default_timer()
    Suma_grupo(0,a,600)
    tiempos.append(timeit.default_timer()-start_time)

plt.plot(a,tiempos,'ro')
plt.axis([0,21,0,1])
plt.ylabel('tiempo en segundos')
plt.xlabel('largo del arreglo')
plt.show()