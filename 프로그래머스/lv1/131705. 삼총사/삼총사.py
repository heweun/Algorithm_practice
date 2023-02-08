from itertools import combinations

def solution(number):
    answer = 0
    
    for a,b,r in combinations(number,3):
        if a+b+r == 0:
            answer += 1
    return answer