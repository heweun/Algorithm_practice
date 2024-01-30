def solution(s):
    answer = ''
    s=s.split(' ')
    for i in range(len(s)):
        # print(f'{s} {i} {s[i]}')
        s[i]=s[i].capitalize() #문자열의 첫글자는 대문자로, 나머지는 소문자로 변환
        # print(f's:{s}')
    answer=' '.join(s)
    return answer