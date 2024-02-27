from collections import Counter
def solution(k, tangerine):
    answer = 0; count = 0
    t_dict = sorted(dict(Counter(tangerine)).items(), key=lambda x: x[1], reverse=True)
    # print(t_dict)

    for t in t_dict:
        # print(f'{t}:{t[1]}')
        count += t[1]
        answer += 1
        if count>=k:
            break
    return answer