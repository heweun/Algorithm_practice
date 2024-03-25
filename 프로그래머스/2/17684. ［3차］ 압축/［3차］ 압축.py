#아흑 길다
#길이==1 ->포함하도록 사전 초기화
#현재 입력과 일치하는 가장 긴 문자열 w 찾기
#w에 해당하는 색인 번호 출력->w제거
#처리되지 않은 다음 글자(c) ->w+c 사전에 추가

def solution(msg):
    answer = []
    # print(ord("A")-64, ord("B")-64, ord("Z")-64)
    w_dic = {chr(i + 64): i for i in range(1, 27)}
    
    w=0; c=0;
    while True:
        c += 1	#1개부터 시작
        if c == len(msg):	
            # print(f'Here {c} == {len(msg)} \n {msg}')
            answer.append(w_dic[msg[w:c]])
            break

        if msg[w:c+1] not in w_dic:
            # print(f'msg[w:c+1]:{msg[w:c+1]}')
            w_dic[msg[w:c+1]] = len(w_dic) +1 #색인 번호 추가
            answer.append(w_dic[msg[w:c]]) #글자 추가
            w = c	#현재 글자를 다음 글자로
            # print(f'w:{w} c:{c}')
    return answer

# A->1 AB->27
# B->2 BA->28
# AB->27 ABA->29
# ABA->29 ABAB->30
# BA->28 BAB->31
# BAB->31 BABA->32
# ABAB->30