from itertools import product

N,M = map(int, open(0).read().split())

for i in product([x for x in range(1,N+1)], repeat = M):
  print(*i)