_,N,*lan = map(int, open(0).read().split())
#print(f'N:{N},n_list:{lan}')

#필요한 인자 지정
start = 1; end = max(lan)

while True:
  if start>end: break

  mid = (start+end)//2
  k = 0
  for l in lan:
    k += l//mid #중간값으로 나눠서 랜선 개수 저장해두기

  #랜선 개수 N과 비교/ 좌우로 움직인다 생각하기
  if k<N:
    end = mid-1
  else:
    start = mid+1

print(end)