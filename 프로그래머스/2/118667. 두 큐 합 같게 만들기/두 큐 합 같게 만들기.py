from collections import deque

#pop == pop(0), insert == append
def solution(queue1, queue2):
    answer = 0
    sum1 = sum(queue1)
    queue1 = deque(queue1); queue2 = deque(queue2)
    standard = sum(queue1+queue2) // 2
    limit = len(queue1) *3
    
    while sum1 != standard:
        #print(f'standard:{standard}, queue1:{sum(queue1)}')
        if sum1<standard:
            num = queue2.popleft()
            queue1.append(num)
            sum1 += num
        elif sum1>standard:
            num = queue1.popleft()
            queue2.append(num)
            sum1 -= num
        answer += 1
        
        if answer == limit:
            return -1
            
    return answer