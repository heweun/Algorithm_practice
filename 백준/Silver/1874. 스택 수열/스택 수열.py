n, *n_list = map(int, open(0).read().split())

cnt = 1
case = True
stack = []
answer = []

for i in n_list:
    while cnt<=i:
        stack.append(cnt)
        answer.append('+')
        cnt += 1

    if stack[-1] == i:
        stack.pop()
        answer.append('-')
    else:
        case = False
        break

if case == False:
    print('NO')
else:
    print(*answer, sep='\n')