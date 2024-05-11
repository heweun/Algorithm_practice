from itertools import permutations

def sosu(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    sosu_set = set()
    for i in range(1,len(numbers)+1):
        for p in permutations(numbers,i):
            sosu_set.add(int("".join(p)))
    # print(f'sosu_set:{sosu_set}')
    for s in sosu_set:
        if sosu(s):
            print(s)
            answer += 1
    return answer