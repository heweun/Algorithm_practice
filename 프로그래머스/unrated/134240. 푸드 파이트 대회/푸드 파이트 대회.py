def solution(food):
    answer=''

    for num, i in enumerate(food):
        for j in range(i//2):
            answer += str(num)
            
    answer=answer + "0" + answer[::-1]
    return answer