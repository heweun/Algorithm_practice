import heapq

def solution(scoville, K):
    answer = 0
    if all(s>=K for s in scoville):
        answer = 0
        
    heapq.heapify(scoville)
    while all(s>=K for s in scoville)==False:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first+second*2)
        answer += 1
        
        if len(scoville)==1 and scoville[0]<K:
            answer = -1
            break
    return answer