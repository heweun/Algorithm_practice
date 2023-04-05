def solution(s, skip, index):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    
    for i in skip:
        alpha = alpha.replace(i,'')
    
    for j in s:
        index_result = alpha.index(j)+index
        if index_result>=len(alpha):
            while index_result>0:
                index_result -= len(alpha)
            answer += alpha[index_result]
        else:
            answer += alpha[index_result]
    return answer