#최소 필요 피로도: 탐험을 위해 최소한의 피로도
#소모 피로도: 탐험 후 소모되는 피로도
#하루에 한 번 탐험 가능한 던전 여러개->최대한 많이
#현재 피로도: k
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for p in permutations(dungeons):
        tmp = k; cnt = 0
        for i,j in p:
            # print(f'i:{i} j:{j}')
            if tmp>=i:
                tmp-=j
                cnt += 1
        # print(f'cnt:{cnt}')
        answer = max(answer, cnt)
    
    return answer