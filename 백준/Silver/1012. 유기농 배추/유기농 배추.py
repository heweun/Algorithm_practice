from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(graph,a,b):
    q = deque()
    q.append((a,b)) #시작점
    graph[a][b] = 0 #이미 방문한 점은 0으로 표기
    count = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=xl or ny<0 or ny>=yl:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
                count += 1
    return count


total,*a = map(int, open(0).read().split())
#print(total,a)

for _ in range(total):
    xl, yl, n = a[:3]
    #print(xl, yl, n)
    ele = a[3:n*2+3]
    #print(ele)

    graph = [[0]*(yl) for _ in range(xl)]
    #print(graph[0])
    for i,j in zip(ele[::2],ele[1::2]):
        #print(i,j)
        graph[i][j]=1
        #print("graph2",graph)
    cnt = []
    for I in range(xl):
        for J in range(yl):
            if graph[I][J]==1:
                cnt.append(dfs(graph,I,J))
    cnt.sort()
    print(len(cnt))

    a = a[n*2+3:]