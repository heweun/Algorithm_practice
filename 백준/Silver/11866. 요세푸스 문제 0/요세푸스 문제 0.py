from collections import deque

N,K = map(int, input().split())
que = deque([x for x in range(1,N+1)])

answer = []

while que:
  for _ in range(K-1):
    que.append(que.popleft())
  answer.append(str(que.popleft()))

print('<'+', '.join(answer)+'>')