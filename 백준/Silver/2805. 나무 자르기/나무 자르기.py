#M 미터의 나무 필요
#H 높이의 절단기
#H보다 큰 만큼만 가져갈 수 있음

_, M, *n_list = map(int, open(0).read().split())

start = 1; end = max(n_list)
while start<=end:
  #print(f'start:{start}, end:{end}')
  mid = (start+end)//2

  pre = 0 #계산한값 비교하기 위해
  for n in n_list:
    if n>=mid:
      pre += n-mid
    else:
      pass
  
  #print(f'pre:{pre}, mid:{mid}')

  if pre>=M:
    start = mid+1
  else:
    end = mid-1

print(end)