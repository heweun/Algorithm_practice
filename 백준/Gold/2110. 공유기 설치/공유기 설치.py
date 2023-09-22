#N개의 집 수직선 위에 존재
#C개의 공유기 설치하려고 함
#한 집에는 공유기 한대만, 가장 인접한 두 공유기 사이의 거리를 가능한 크게
#숫자는 실제 거리라고 보면 됨

N, C, *n_list = map(int, open(0).read().split())
n_list.sort()
start = 1; end = n_list[-1]-n_list[0]
result = 0

while start<=end:
  mid = (start+end)//2
  cur = n_list[0] #첫번째 값부터 시작

  cnt = 1
  for i in range(1,N):
    if n_list[i]>=cur+mid: #다음번째 값이 시작값에 mid를 더한것보다 크면
      cur = n_list[i] #공유기 설치
      cnt += 1 #공유기 개수 늘리기

  #print(f'cnt:{cnt}')
  if cnt>=C:
    start = mid+1
  else:
    end = mid-1

print(end)