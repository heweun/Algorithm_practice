def solution(numbers):
    num_dic = {i:0 for i in range(10)}
    answer = -1
    
    for num in numbers:
        num_dic[num]+=1
    
    answer = sum(i for i in range(10) if num_dic[i]==0)
    
    return answer 