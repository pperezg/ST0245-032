def opciones1por2(n):
    if n<=2:
        return n
    else:
        return opciones1por2(n-2) + opciones1por2(n-1)


print(opciones1por2(5))