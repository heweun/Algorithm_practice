#최대 힙 : 배열에 자연수 X를 넣는다 -> 배열에서 가장 큰 값 출력, 그 값 제거
#N: 연산의 개수
#x가 자연수 이면 배열에 x추가 / x가 0이면 pop(x) * 값이 비어있으면 0출력

##최소힙이 기준인
#heapq 함수 활용하기
#heappush(heap, item) : item을 heap에 추가
#heapop(heap) : 가장 작은 원소 pop, 비어있는 경우 indexError
#heapify(x) : 리스트 x를 heap으로 변환

##최대힙을 구현하기 위해선 원소 추가시 (-item, item)의 튜플 형태로 넣어줌

_, *n_list = map(int, open(0).read().split())
from heapq import *

heap = []
for n in n_list:
  if n != 0:
    heappush(heap, -n)
  else:
    if heap:
      print(abs(heappop(heap)))
    else:
      print(0)