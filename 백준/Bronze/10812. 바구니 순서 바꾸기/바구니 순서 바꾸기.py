N, M = map(int,input().split())

num_list = [i for i in range(1,N+1)]

for _ in range(M):
  i,j,k = map(int,input().split())
  for n in num_list[k-1:j][::-1]:
    del num_list[num_list.index(n)]
    num_list.insert(i-1,n)

print(*num_list)