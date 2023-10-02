from heapq import *
_, *n_list = map(int, open(0).read().split())

heap = []

for n in n_list:
  if n != 0:
    heappush(heap, n)
  else:
    if heap:
      print(heappop(heap))
    else:
      print(0)