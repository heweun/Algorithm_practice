def solution(A,B):
    answer = 0
    # print(f'A:{sorted(A)} B:{sorted(B)}')
    A,B = sorted(A),sorted(B)
    for a,b in zip(A,B[::-1]):
        # print(f'a:{a} b:{b}')
        answer += a*b
    return answer