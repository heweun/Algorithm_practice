d = [[[0] * 21 for _ in range(21)] for _ in range(21)]
#계산한 값을 미리 넣어둔다! / 20보다 크면 --> 20이 되니까 그 범위까지 제작

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if (d[a][b][c] != 0): #이미 계산된 값이면 출력하기-->시간줄이는 key
        #print(f'a,b,c:{a, b, c},d:{d},{d[a][b][c]}')
        return d[a][b][c]
    if a < b < c:
        d[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        d[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    #print(f'a,b,c:{a,b,c},d:{d},{d[a][b][c]}')
    return d[a][b][c]

*N,end = ([*map(int, i.split())] for i in open(0))
for n in N:
    a = n[0]; b = n[1]; c = n[2]
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')