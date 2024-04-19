def solution(land):
    answer = 0
    
    for i in range(1,len(land)):
        for j in range(len(land[0])):
            # print(f'i:{i} j:{j} land:{land[i][j]}')
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
            
    # print(f'land:{land}')
    answer = max(land[-1])
    return answer