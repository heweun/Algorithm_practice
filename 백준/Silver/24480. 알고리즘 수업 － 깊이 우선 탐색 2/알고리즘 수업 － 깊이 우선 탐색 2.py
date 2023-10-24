import sys
sys.setrecursionlimit(10**6) #재귀의 깊이 제한하기

N,*n_list=([*map(int,i.split())]for i in open(0))

n = N[0]; r = N[2]
graph = [[]for _ in range(n+1)]
visited = [0]*(n+1)

#데이터 넣어두기
for n in n_list:
  graph[n[0]].append(n[1])
  graph[n[1]].append(n[0])

#내림차순 정렬
graph = [sorted(g, reverse=True) for g in graph]
#print(f'graph:{graph}')

#dfs
c = 1 #방문 여부 뿐만 아니라 순서까지 나타내기 위해
def dfs(visited,graph,r):
  global c
  #print(f'visited:{visited}, graph:{graph}, r:{r}')
  visited[r] = c
  #print(f'visited:{visited}')
  for x in graph[r]:
    #print(f'x:{x}')
    if visited[x] == 0: #방문 안했으면
      c += 1
      dfs(visited, graph, x)

dfs(visited, graph, r)

for v in visited[1:]:
  print(v)