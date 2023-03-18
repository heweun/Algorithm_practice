def solution(dartResult):
    answer = []
    score = ["S","D","T"]
    dartResult = dartResult.replace("10", "A")
    dart_list = ["10" if i=="A" else i for i in dartResult]
    
    i=-1
    for d in dart_list:
        if d.isnumeric() == True:
            answer.append(int(d))
            i += 1
        elif d in score:
            answer[i] = answer[i]**(score.index(d)+1)
        elif d == "#":
            answer[i] = answer[i]*-1
        else:
            answer[i] = answer[i]*2
            if i!=0:
                answer[i-1] = answer[i-1]*2
                
    return sum(answer)