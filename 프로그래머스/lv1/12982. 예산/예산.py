def solution(d, budget):
    answer = 0
    
    while sum(d)>budget:
        d.remove(max(d))
        
    answer = len(d)
    return answer