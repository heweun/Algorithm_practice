def solution(s):
    br = [0]
    
    for i in s:
        if br[-1] == '(' and i == ')':
            br.pop()
        else:
            br.append(i)
        # print(br)

    return len(br)<=1