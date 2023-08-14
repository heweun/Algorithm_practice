from itertools import combinations

N,M  = map(int, open(0).read().split())
a = list(combinations([x for x in range(1,N+1)],M))

for i in a:
  print(*i)