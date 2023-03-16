origin  = [1,1,2,2,2,8]
have = list(map(int, input().split()))

result = [j-i for i,j in zip(have, origin)]
print(*result)