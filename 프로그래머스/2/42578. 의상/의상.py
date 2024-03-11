from collections import Counter

def solution(clothes):
    answer = 1
    c_dict = Counter([c[1] for c in clothes])
    # print(c_dict)
    
    for cloth in c_dict.values():
        answer *= (cloth+1)
        # print(f'cloth:{cloth}, answer:{answer}')

    return answer-1