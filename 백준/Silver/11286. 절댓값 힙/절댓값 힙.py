from heapq import *
_, *n_list = map(int, open(0).read().split())
#print(f'n_list:{n_list}')

heap = []
for n in n_list:
  if n != 0:
    heappush(heap, (abs(n),n))
  else:
    if heap:
      print(heappop(heap)[1])
    else:
      print(0)