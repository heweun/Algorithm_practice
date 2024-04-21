from collections import Counter

def solution(topping):
    answer = 0
    dic = Counter(topping) #숫자를 세어 두기
    set_dic = set()
    
    for i in topping:
        dic[i] -= 1 #한번 셋으니까 개수 줄이고
        set_dic.add(i) #새로운 곳에 넣기(왼쪽이라고 생각)
        if dic[i] == 0: #해당 토핑을 이미 새로운 곳에 다 넣었다면
            dic.pop(i) #딕셔너리에서 지워주기
        if len(dic) == len(set_dic): #왼쪽 오른쪽(딕셔너리) 길이가 같아지면
            answer += 1 #성공개수로 추가
    
    return answer