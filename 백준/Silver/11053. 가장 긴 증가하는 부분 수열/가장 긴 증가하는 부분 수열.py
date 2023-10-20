n, *N = map(int, open(0).read().split())

dp = [1]*n

for i in range(1,n):
  for j in range(i):
    #print(f'i:{i}, j:{j}')
    if N[i]>N[j] and dp[i]<dp[j]+1:
      #print(f'N[{i}]:{N[i]}, N[{j}]:{N[j]}, dp:{dp}')
      dp[i] = dp[j]+1

print(max(dp))