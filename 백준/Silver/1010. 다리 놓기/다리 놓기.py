import math

N = int(input())

for _ in range(N):
  A = list(map(int, input().split()))
  print(math.comb(max(A),min(A)))