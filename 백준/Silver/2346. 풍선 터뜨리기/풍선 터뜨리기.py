from collections import deque

_, *n_list  = map(int, open(0).read().split())

a = deque(enumerate(n_list))
ans = []

while a:
  idx, number = a.popleft()
  ans.append(idx+1)

  if number > 0:
    a.rotate(-(number-1))
  else:
    a.rotate(-number)

print(*ans)