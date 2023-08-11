from itertools import permutations

A, B = map(int, open(0).read().split())
num_list = [x for x in range(1,A+1)]

for n in list(permutations(num_list,B)):
  print(*n)