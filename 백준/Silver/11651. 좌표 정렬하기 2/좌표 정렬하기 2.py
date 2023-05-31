n,*L=([*map(int,i.split())]for i in open(0))
L = sorted(L, key=lambda x:(x[1],x[0]))
for l in L:
    print(*l)