def solution(N, stages):
    n_dic = {i:0 for i in range(1,N+1)}
    result = len(stages)
    
    for i in range(1,N+1):
        if result != 0:
            n_dic[i] = stages.count(i)/result
            result -= stages.count(i)
        else:
            n_dic[i] = 0
    answer = sorted(n_dic,key = lambda x:n_dic[x],reverse=True)
    return answer