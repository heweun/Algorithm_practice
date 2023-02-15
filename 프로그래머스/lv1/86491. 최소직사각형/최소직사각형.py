def solution(sizes):
    answer = 0
    
    w_list = [max(i) for i in sizes]
    h_list = [min(i) for i in sizes]
    
    answer = max(w_list)*max(h_list)
    
    return answer