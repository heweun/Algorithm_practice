import sys
from collections import deque
sys.setrecursionlimit(10**6) #재귀의 깊이 제한하기

n,_,*n_list=([*map(int,i.split())]for i in open(0))

r = 1
graph = [[]for _ in range(n[0]+1)]
visited = [0]*(n[0]+1)
answer = 0

#데이터 넣어두기
for n in n_list:
  graph[n[0]].append(n[1])
  graph[n[1]].append(n[0])

#print(f'graph:{graph}')
#bfs
c = 1
def bfs(visited,graph,r):
  global c,answer
  visited[r] = c
  que = deque([r])
  while que:
    #print(f'que:{que}')
    answer += 1
    u = que.popleft() #맨 앞 요소 삭제
    for x in graph[u]: #빼낸 요소 주변 확인
      if visited[x] == 0: #방문 안했으면
        que.append(x)
        c += 1
        visited[x] = c


bfs(visited,graph,r)

print(answer-1)