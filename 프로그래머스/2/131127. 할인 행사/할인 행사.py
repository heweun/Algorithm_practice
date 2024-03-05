from collections import Counter
def solution(want, number, discount):
    answer = 0
    w_dic = {w:n for w,n in zip(want, number)}
    
    for i in range(len(discount)-9):
        d_list = discount[i:10+i]
        if Counter(d_list) == w_dic:
            # print(f'Counter(d_list):{Counter(d_list)}, w_dic:{w_dic}')
            answer += 1
    
    return answer