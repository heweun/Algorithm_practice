from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    count = 0
    while queue:
        #print(f'queue:{queue}, count:{count}, m:{m}')

        if max(queue) == queue[0]: # 맨앞 숫자가 가장클때
            queue.popleft() #하나 출력
            count += 1 # 하나가 영원히 배출되므로 순번은 하나 추가
            m -= 1 #순서는 하나 앞으로

            if m < 0: # m이 0이면 -> m이 queue의 최대값이 됨
                print(count)
                break #종료

        else:   # 첫번째가 가장 크지 않으면
            queue.rotate(-1) # 순서 바꿔주고
            m -= 1 #내 위치는 당겨오기
            if m<0: #만약에 맨 앞에 있는데 최대값이 아니면
              m = len(queue)-1 #맨 뒤 순서로 바뀜