def solution(s):
    answer = 0
    stack = [s[0]]
    
    for i in s[1:]:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    
    if len(stack) == 0: answer = 1
    
    return answer