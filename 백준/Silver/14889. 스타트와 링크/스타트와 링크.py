import sys

input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
res = 1e9

def DFS(L, idx):
    global res
    if L == N // 2:
        #print("\n#I'm here2#")
        #print(f'L:{L}')
        A = 0; B = 0
        for i in range(N):
            for j in range(N):
                #print(f'i:{i}, j:{j}, visited:{visited[i], visited[j]}, visited:{visited}')
                if visited[i] and visited[j]:
                    A += board[i][j]
                    #print(f'A:{A}')
                elif not visited[i] and not visited[j]:
                    B += board[i][j]
                    #print(f'B:{B}')
        res = min(res, abs(A - B))
        #print(f'res:{res}')
        return

    for i in range(idx, N):
        #print("\n#I'm here1#")
        #print(f'idx:{idx}, N:{N}, i:{i},visited[{i}]:{visited[i]}')
        if not visited[i]:
            #print(f'visited[{i}]:{visited[i]}, visited:{visited}')
            visited[i] = True
            DFS(L + 1, i + 1)
            visited[i] = False #다시 원위치 시키기


DFS(0, 0)
print(res)