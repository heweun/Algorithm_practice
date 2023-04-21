from collections import deque

n = int(input())
m = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
  a,b = map(int, input().split())
  graph[a][b] = graph[b][a] = 1

v = 1
q = deque()
q.append(v)

while q:
  v = q.popleft()
  for i in range(1,n+1):
    if visited[i] == 0 and graph[v][i] == 1:
      q.append(i)
      visited[i] = 1

print(visited.count(1)-1)