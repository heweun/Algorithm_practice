#왜이렇게 문제를 길게 내냐..
#두 사람 선물 기록 있음&선물 개수가 다를때->더 많이 준 사람이 다음달에 하나 받음
#두 사람 선물 기록 없음&선물 기록이 같을때->선물 지수가 더 큰 사람이 다음달에 하나 받음
#선물 지수 == 준 선물-받은 선물
#단, 선물 지수도 같으면 선물 주고 받기X
#선물 가장 많이 받을 친구가 받을 선물 수 출력

# def solution(friends, gifts):
#     answer = 0
#     g_dic = {x:[0 for _ in range(len(friends)+1)] for x in friends} #입력할 공간 마련
#     g_index = {x:0 for x in friends} #
#     c_dic = {x:0 for x in friends} #다음달 받을 선물 개수
    
#     for g in gifts:
#         g = g.split()
#         dic[g[0]][friends.index(g[1])] += 1 #선물 주기
#         dic[g[0]][-1] += 1 #준 사람 선물 지수 +1
#         dic[g[1]][-1] -= 1 #받은 사람 선물 지수 -1
#     print(dic)
    
#     for i,f in enumerate(friends):
#         print(f'name:{f} {i}번째')
#         for j in dic[f]:
#             if j>dic[]
#             print(j)
   
        
#     return answer

def solution(friends, gifts):
    answer = 0
    length = len(friends)
    score = [0] * len(friends)

    #0. Create Table
    give = [[0] * length for _ in range(length)] # 인원수별 선물 확인할 이중리스트 제작
    for gift in gifts:
        gift = gift.split(" ")
        giver = friends.index(gift[0])
        getter = friends.index(gift[1])

        give[giver][getter] += 1 #누구에게 줬는지 확인하며 +1
    # print(f'final give:{give}') #선물 주고 받은 리스트

    for i in range(length):
        for j in range(i + 1, length):
            # print(f'i:{i}, j:{j}')
            give_score = give[i][j] # i가 j에게 준 선물의 개수
            get_score = give[j][i] #j가 i에게 준 선물의 개수
            # print(f'give_score:{give_score}, get_score:{get_score}')

            #give와 get비교하기
            if (give_score != get_score) and (give_score > 0 or get_score > 0):
                #둘이 주고 받은게 다르고, 0보다 클때
                if give_score > get_score:
                    score[i] += 1 #giver가 받음

                else:
                    score[j] += 1 #getter가 받음

            #0이거나, 동점일때 선물 지수 확인
            else:
                # print(f'give[{i}]:{give[i]} give[{j}]:{give[j]}')
                giver_present_score = sum(give[i])
                getter_present_score = sum(give[j])
                
                # print(f'giver_present_score:{giver_present_score}\ngetter_present_score:{getter_present_score}')
                for k in range(length):
                    giver_present_score -= give[k][i]
                    getter_present_score -= give[k][j]

                if giver_present_score > getter_present_score:
                    score[i] += 1

                elif giver_present_score < getter_present_score:
                    score[j] += 1

    answer = max(score)
    return answer