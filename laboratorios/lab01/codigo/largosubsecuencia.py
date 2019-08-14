def largosubsecuencia(a, b):
    if (len(a)==0) or (len(b)==0):
        return 0
    elif (a[0]==b[0]):
        return 1 + largosubsecuencia(a[1:],b[1:])
    else:
        return max(largosubsecuencia(a[1:],b),largosubsecuencia(a,b[1:]))


print(largosubsecuencia('adgjkl','afehjkl'))