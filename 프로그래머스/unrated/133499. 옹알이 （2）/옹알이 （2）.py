def solution(babbling):
    baby_can = ["aya", "ye", "woo", "ma" ]
    answer = 0
    
    for word in babbling:
        for word_can in baby_can:
            if word_can*2 not in word:
                word = word.replace(word_can, "F")
        
        if len(word.strip("F"))==0:
            answer+=1
    return answer