def solution(answers):
    list_1 = [1,2,3,4,5]
    list_2 = [2,1,2,3,2,4,2,5]
    list_3 = [3,3,1,1,2,2,4,4,5,5]
    dic = {1:0,2:0,3:0}
    
    for i in range(len(answers)):
        if answers[i] == list_1[i%5]:
            dic[1] += 1
        if answers[i] == list_2[i%8]:
            dic[2] += 1
        if answers[i] == list_3[i%10]:
            dic[3] += 1
    
    answer = [k for k,v in dic.items() if max(dic.values())==v]
    return answer