import sys
from collections import deque
sys.setrecursionlimit(10**6) #재귀의 깊이 제한하기

N, *n_list=([*map(int,i.split())]for i in open(0))

n = N[0]; r= N[2]
graph = [[]for _ in range(n+1)]
visited_dfs = [0]*(n+1)
visited_bfs = [0]*(n+1)
c = 1

#데이터 넣어두기
for n in n_list:
  graph[n[0]].append(n[1])
  graph[n[1]].append(n[0])
#print(f'graph:{graph}')

#정렬하기
graph = [sorted(g) for g in graph]

#bfs
def bfs(visited_bfs,graph,r):
  global c
  visited_bfs[r] = c
  que = deque([r])
  while que:
    u = que.popleft() #맨 앞 요소 삭제
    print(u, end=' ')
    for x in graph[u]: #빼낸 요소 주변 확인
      if visited_bfs[x] == 0: #방문 안했으면
        que.append(x)
        c += 1
        visited_bfs[x] = c

#dfs
def dfs(visited_dfs,graph,r):
  global c
  visited_dfs[r] = c
  print(r, end=' ')
  for x in graph[r]: #빼낸 요소 주변 확인
    if visited_dfs[x] == 0: #방문 안했으면
      c += 1
      dfs(visited_dfs,graph,x)

dfs(visited_dfs,graph,r)
print()
bfs(visited_bfs,graph,r)