from math import sqrt

def sosu(num):
  if num == 1:
    return False
  for n in range(2,int(sqrt(num))+1):
    if num%n == 0:
      return False
  return True

M,N = map(int,input().split())
for num in range(M,N+1):
  if sosu(num):
    print(num)
  else:
    pass