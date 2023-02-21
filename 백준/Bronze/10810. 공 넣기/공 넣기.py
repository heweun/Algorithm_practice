import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = [0 for _ in range(N)]

for m in range(M):
    i,j,k = map(int, input().split())
    for num in range(i-1,j):
        N_list[num]=k

print(*N_list)