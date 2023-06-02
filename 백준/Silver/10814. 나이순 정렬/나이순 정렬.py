user = sorted([i.split() for i in open(0)][1:], key=lambda x:int(x[0]))
for u in user:
    print(*u)