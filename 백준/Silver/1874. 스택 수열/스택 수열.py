n, *n_list = map(int, open(0).read().split())

cnt = 1
stack = []
answer = []

for i in n_list:
    while cnt<=i:
        stack.append(cnt)
        answer.append('+')
        cnt += 1

    if stack.pop() != i:
        answer = 'NO'
        break
    else:
        answer.append('-')
else:
    answer = '\n'.join(answer)

print(answer)