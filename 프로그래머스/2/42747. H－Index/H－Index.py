def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)
    #print(citations)
    if max(citations) == 0:
        answer = 0
    else:
        for i in range(1,len(citations)+1)[::-1]:
            # print(i)
            if min(citations[:i]) >= i:
                # print(f'{i}는 {citations[:i]}')
                answer = i
                break
    return answer