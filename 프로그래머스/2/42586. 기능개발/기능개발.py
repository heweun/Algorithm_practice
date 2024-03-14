import math
# from collections import deque

def solution(progresses, speeds):
    answer = []
    start = math.ceil((100-progresses[0])/speeds[0])
    cnt = 0
    
    for p,s in zip(progresses, speeds):
        # print(f'{100-p}완성하기 위해 {math.ceil((100-p)/s)}일 필요')
        # print(math.ceil((100-p)/s))
        if math.ceil((100-p)/s)>start:
            answer.append(cnt)
            start = math.ceil((100-p)/s)
            cnt = 1
            # print(f'if {math.ceil((100-p)/s)}, {start}, answer:{answer}')
        else:
            # print(f'else {math.ceil((100-p)/s)}, {start}, answer:{answer}')
            cnt += 1
    answer.append(cnt)
    return answer