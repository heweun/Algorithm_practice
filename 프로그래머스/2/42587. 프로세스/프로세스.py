#하나를 꺼낸다->우선순위 비교
#1. 우선순위 낮다->다시 큐에 넣기
#2. 우선순위 높다->프로세스 실행
#숫자 클수록 우선 순위 높음

from collections import deque

def solution(priorities, location):
    answer = 0
    dq = deque([(value, idx) for idx, value in enumerate(priorities)]) #튜플로 넣어서 원래 순서 남겨두기
    #print(f'dq:{dq}')
    
    while dq:
        item = dq.popleft()
        #print(f'item:{item}')
        if any(item[0] < other[0] for other in dq):
            dq.append(item)
            #print(f'추가된 dq:{dq}')
        else:
            answer += 1 #프로세스 실행
            #print(f'프로세스 실행 item:{item} location:{location} answer:{answer}')
            if item[1] == location: #위치 나오면->프로세스 진행된 횟수 출력
                return answer