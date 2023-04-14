num,*num_list = map(int,open(0).read().split())

answer = 0
for n in num_list:
    yaksu = 0
    for i in range(1,n):
        if n%i == 0:
            yaksu += 1
    if yaksu == 1:
        answer += 1

print(answer)