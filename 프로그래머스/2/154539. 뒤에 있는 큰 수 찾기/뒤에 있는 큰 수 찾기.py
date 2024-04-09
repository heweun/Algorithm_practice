def solution(numbers):
    answer = [-1]*len(numbers)
    stack = []
    
    for i,num in enumerate(numbers):
        # print(f'i:{i}, num:{num} stack:{stack}')
        while stack and numbers[stack[-1]]<num:
            # print(f'stack:{stack} num:{num}')
            answer[stack.pop()] = num
        stack.append(i)
        # print(f'pure_stack:{stack}')
        
    return answer