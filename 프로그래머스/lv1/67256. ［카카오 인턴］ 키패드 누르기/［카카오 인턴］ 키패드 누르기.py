def solution(numbers, hand):
    dic = {1:[1,4],2:[2,4],3:[3,4],4:[1,3],5:[2,3],
       6:[3,3],7:[1,2],8:[2,2],9:[3,2],0:[2,1]}
    l = [1,1]
    r = [3,1]
    hand = 'L' if hand =="left" else "R"
    
    answer = ''
    
    for i in numbers:
        if dic[i][0]==1:
            answer += "L"
            l=dic[i]
        elif dic[i][0]==3:
            answer += "R"
            r=dic[i]

        else:
            left_side = abs(l[0]-dic[i][0])+abs(l[1]-dic[i][1])
            right_side = abs(r[0]-dic[i][0])+abs(r[1]-dic[i][1])
            if left_side<right_side:
                answer += "L"
                l=dic[i]
            elif left_side>right_side:
                answer += "R"
                r=dic[i]
            else:
                answer += hand
                if hand == "L":
                    l = dic[i]
                else:
                    r = dic[i]
    return answer