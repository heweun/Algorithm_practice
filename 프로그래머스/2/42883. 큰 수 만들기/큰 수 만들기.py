def solution(number, k):
    answer = [] 
    
    for num in number:
        # print(f'num:{num} answer:{answer}')
        while k > 0 and answer and answer[-1] < num:
            # print("I'm in")
            answer.pop()
            k -= 1
        answer.append(num)
        # print(f'\nafter_answer:{answer}\n')
        
    return ''.join(answer[:len(answer) - k])