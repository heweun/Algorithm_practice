import sys
from collections import deque
sys.setrecursionlimit(10**6) #재귀의 깊이 제한하기

N,*n_list=([*map(int,i.split())]for i in open(0))

n = N[0]; r = N[2]
graph = [[]for _ in range(n+1)]
visited = [0]*(n+1)

#데이터 넣어두기
for n in n_list:
  graph[n[0]].append(n[1])
  graph[n[1]].append(n[0])

#오름차순 정렬
graph = [sorted(g) for g in graph]
#print(f'graph:{graph}')

#bfs
c = 1 #방문 여부 뿐만 아니라 순서까지 나타내기 위해
def bfs(visited,graph,r):
  global c
  visited[r] = c
  que = deque([r])
  while que:
    #print(f'graph:{graph}, que:{que}, visited:{visited}')
    u = que.popleft() #맨 앞 요소 삭제
    for x in graph[u]: #빼낸 요소 주변 확인
      if visited[x] == 0: #방문 안했으면
        que.append(x)
        c += 1
        visited[x] = c


bfs(visited,graph,r)

for v in visited[1:]:
  print(v)