A,*N = open(0)
dance = {'ChongChong'}

for i in N:
    a,b = i.split()
    if a in dance:
        dance.add(b)
    if b in dance:
        dance.add(a)

print(len(dance))
