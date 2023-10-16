n, *n_list = map(int, open(0).read().split())

dp = [0]*301

if len(n_list)<=2: # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(n_list))

else:
  dp[0] = n_list[0]
  dp[1] = n_list[0]+n_list[1]
  dp[2] = max(n_list[0]+n_list[2], n_list[1]+n_list[2])

  #거꾸로 n번째 계단에 올라섰을때 어디서 왔는지 확인하기
  for i in range(3, n):
    dp[i] = max(dp[i-3]+n_list[i-1]+n_list[i], dp[i-2]+n_list[i])
    #1번째 전에서 왔으면 -> 무조건 두번째 전+첫 번째 전
    #2번째 전에서 왔으면 -> 상관없음

  print(dp[n-1])