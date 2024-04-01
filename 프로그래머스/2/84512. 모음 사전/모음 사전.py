#중복 순열
from itertools import product

def solution(word):
    answer = 0
    
    result = list()
    for i in range(1,6):
        li = list(product(['A', 'E', 'I', 'O', 'U'], repeat = i)) #1개부터 5개까지 확인하기 위함
        # print(f'{i}li:{li}')
        for j in li:
            result.append(''.join(k for k in j))
            #원소 이어서 하나의 단어로 만들기
    
    result.sort() #사전순으로 정렬하기
    answer = result.index(word) + 1
    return answer