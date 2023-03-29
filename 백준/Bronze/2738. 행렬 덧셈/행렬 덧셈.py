N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
b = [list(map(int, input().split())) for _ in range(N)]

for row in range(N):
    for col in range(M):
        print(a[row][col] + b[row][col], end=' ')
    print()