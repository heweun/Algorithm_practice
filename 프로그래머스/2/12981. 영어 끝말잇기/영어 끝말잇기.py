def solution(n, words):
    answer = [0,0] #다 통과되면 default
    w_list = [words[0]] #단어 확인용 리스트
    last = words[0][-1] #끝 알파벳 확인용 리스트
    who = 1 #누가 걸렸는지 확인하기 위함
    #print(f'w_list:{w_list} last:{last}')
    
    for w in words[1::]:
        if w[0] == last and w not in w_list:
            w_list.append(w)
            last = w[-1]
            who += 1
            #print(f'new w_list:{w_list} last:{last} who:{who}')
        else:
            #print(f'걸림:{who} 단어:{w}')
            answer = [n if (who+1)%n == 0 else (who+1)%n,
                      (who+1)//n if (who+1)%n==0 else (who+1)//n+1]
            break
            
    return answer