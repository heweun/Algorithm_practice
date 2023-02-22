M, N = map(int, input().split())
M_list = [m for m in range(1,M+1)]

for n in range(N):
    i, j = map(int, input().split())
    M_list[i-1], M_list[j-1] = M_list[j-1], M_list[i-1]

print(*M_list)