def hanoi(topN, a, b, c):
    if topN==1:
        print("Move top disk from "+a+" to "+c)
    else:
        hanoi(topN-1,a,c,b)
        print("Move top disk from "+a+" to "+c)
        hanoi(topN-1,b,a,c)


print(hanoi(4,"Left","Centre","Right"))
