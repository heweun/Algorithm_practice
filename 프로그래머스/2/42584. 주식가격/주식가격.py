def solution(prices):
    answer = [i for i in range(0,len(prices))[::-1]]
    # print(f'answer:{answer}')
    stack = []
    
    for i,num in enumerate(prices):
        while stack and prices[stack[-1]]>num:
            j = stack.pop()
            answer[j] = i-j
        stack.append(i)
    return answer