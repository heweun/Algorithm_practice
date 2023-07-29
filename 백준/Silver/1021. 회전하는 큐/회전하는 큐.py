from collections import deque
A,B,*X = map(int, open(0).read().split())

a = deque([x for x in range(1,A+1)])
X = deque(X)

cnt = 0
while X:
  if X[0] == a[0]:
    a.popleft();X.popleft()
  else:
    if a.index(X[0])>len(a)//2:
      a.rotate(1)
      cnt += 1
    else:
      a.rotate(-1)
      cnt += 1

  #print(f'X:{X},a:{a},cnt:{cnt}')

print(cnt)