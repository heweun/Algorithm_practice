#t초 동안 붕대 감으면->1초마다 x만큼 체력 회복 == t*x회복
#t초 연속 붕대 감기 성공->y만큼 체력 추가 회복 단, 최대 체력보다 커지면 안됨
#기술 쓰던 중 공격->기술 취소->체력회복 불가->연속 성공 0초로 리셋->붕대 감기 다시
#몬스터 공격->체력 감소->0이하가 되면 죽음
#문제: 붕대감기 기술 정보+캐릭터 최대체력+몬스터 공격패턴 == 캐릭터 생존 여부
#결과: 모든 공격이 끝난 후 남은 체력 return / 0이하 -1

def solution(bandage, health, attacks):
    answer = health
    max_att = attacks[-1][0]+1 #마지막 공격 지정
    att_dic = dict(attacks) #딕셔너리로 변경
    cnt_band = 0 #연속 붕대 감기 계산용
    
    for i in range(1,max_att):
        if i in att_dic:
            answer -= att_dic[i]
            cnt_band = 0
            if answer <= 0:
                answer = -1
                break
        
        else:
            cnt_band += 1
            answer += bandage[1]
            if cnt_band == bandage[0]:
                answer += bandage[2]
                cnt_band = 0
            answer = min(answer, health)
            
    return answer