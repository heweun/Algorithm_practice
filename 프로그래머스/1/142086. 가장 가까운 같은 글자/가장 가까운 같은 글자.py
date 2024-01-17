def solution(s):
    v_dic = {} #위치 담아두기 용
    answer = []
    
    for i,w in enumerate(s):
        # print(f'i:{i}, w:{w}')        
        if w not in v_dic:
            answer.append(-1)
        else:
            answer.append(i-v_dic[w])
        v_dic[w] = i
            
        # print(f'v_dic:{v_dic} answer:{answer}')
    return answer