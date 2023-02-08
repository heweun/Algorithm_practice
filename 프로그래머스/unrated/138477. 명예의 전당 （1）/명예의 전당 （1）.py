def solution(k, score):
    answer = []
    compare=[]
    for i in score:
        compare.append(i)
        if len(compare)>k:
            compare.remove(min(compare))
        answer.append(min(compare))
    return answer