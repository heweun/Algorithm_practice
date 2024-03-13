def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{") #한 번에 이어서 하지 말 것
    s.sort(key = len) #재 지정 필요 없음
    #print(s)
    for i in s:
        for j in i.split(","):
            # print(f'{i}, {i.split(",")}:{j}')
            if int(j) not in answer: #int로 형변환 필수!
                answer.append(int(j))
                # print(f'answer:{answer}')
    
    return answer