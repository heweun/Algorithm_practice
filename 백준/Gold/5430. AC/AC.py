#R(뒤집기) 배열에 있는 수의 순서를 뒤집는 함수
#D(버리기) 첫번째 수를 버리는 함수 단, 비어있으면 에러 발생
from collections import deque
n, *A = open(0).read().split()

for a,c in zip(A[0::3],A[2::3]):
  if c == '[]': #첫번째 비어있는지 확인 먼저!
    c = []
  else:
    c = deque(c[1:-1].split(',')) #문자로 읽기 때문에 범위 나눠서 split()

  flag = True #error발생 여부 확인용
  reverse_count = 0 #R가 짝수(뒤집기 없음)/홀수(뒤집기) 짝홀 확인용

  for i in a:
    if i == 'R':
      reverse_count += 1 #짝홀 확인하기
    
    #len(c)가 0이 아니고+R이 짝수이면 뒤집기 없음-->popleft()
    #len(c)가 0이 아니고+R이 홀수이면 뒤집기 있음-->pop() *뒤가 앞이 되니까
    elif i == 'D': 
      if c:
        if reverse_count %2 == 0:
          c.popleft()
        else:
          c.pop()
      
      #len(c)가 0이면 flag --> False로 변경 --> error출력
      else:
        flag = False
        break

  if flag: #결과 출력 R이 홀수이면-->reverse하고 출력
    if reverse_count %2 == 1:
      c.reverse()
    print("[" + ",".join(c) + "]")
  else:
    print('error')