from collections import deque

def solution(cacheSize, cities):
    answer = 0
    dq = deque(maxlen=cacheSize) #deque maxlen 설정하기!
    
    if cacheSize == 0:
        answer = len(cities) * 5
    else:
        for c in cities:
            c = c.lower()
            if c in dq:
                dq.remove(c)
                answer += 1
            else:
                answer += 5
            dq.append(c) #항상 넣어줘야함
            #print(f'dq:{dq}')
            
    return answer
