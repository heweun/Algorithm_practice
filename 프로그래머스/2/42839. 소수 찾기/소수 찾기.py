from itertools import permutations

def sosu(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    b_list = set()
    for a in range(1,len(numbers)+1):
       for p in permutations(numbers,a):
        b_list.add(int("".join(p)))
    # print(b_list)
    for b in b_list:
        if sosu(b):
            answer += 1
    return answer