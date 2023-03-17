from itertools import combinations

def solution(nums):
    answer = 0
    
    for num in combinations(nums, 3):
        yaksu = 0
        for i in range(2, sum(num)//2):
            if sum(num)%i == 0:
                yaksu += 1
        if yaksu == 0:
            answer += 1

    return answer