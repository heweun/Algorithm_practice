from itertools import combinations_with_replacement
N,M = map(int, open(0).read().split())

for a in combinations_with_replacement([x for x in range(1,N+1)], M):
    print(*a)