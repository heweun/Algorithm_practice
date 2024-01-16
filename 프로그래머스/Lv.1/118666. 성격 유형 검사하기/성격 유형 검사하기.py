def solution(survey, choices):
    answer = ''
    # c_dic = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3} 
    s_dic = {'R':0, 'T':0,'C':0, 'F':0,'J':0, 'M':0,'A':0, 'N':0}
   
    for a,c in zip(survey, choices):
        #print(f'a:{a}, c:{c}')
        if c>=4:
            s_dic[a[1]] += c-4
        else:
            s_dic[a[0]] += 4-c
    
    li = list(s_dic.items()) #인덱싱을 위해 리스트로 가져오기
    
    for i in range(0,8,2): #두개씩 묶기 위해 짝수로 범위 제한
        if li[i][1]<li[i+1][1]:
            answer += li[i+1][0]
        else:
            answer += li[i][0]
    return answer