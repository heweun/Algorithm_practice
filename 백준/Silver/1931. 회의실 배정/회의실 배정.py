#한 개의 회의실을 사용하고자하는 N개의 회의
#각 회의 I(시작시간,끝나는시간)
#회의 시작과 끝나는 시간이 같을 수 있지만, 겹치지 않게 최대한 많이

N,*n_list = ([*map(int, i.split())] for i in open(0))
N = N[0] #숫자로 지정해두기
n_list.sort(key = lambda x:(x[1],x[0])) #일단 정렬 단, 끝나는 시간 기준으로 할 것
#print(n_list)

#가장 빨리 끝나는 첫번째 회의는 무조건 선택-->다른 경우를 보지 않는것이 시간단축
selected = [n_list[0]]
end_time = n_list[0][1]
#print(f'selected:{selected}, end_time:{end_time}')

for i in range(1,N):
    if n_list[i][0]>=end_time:
        selected.append(n_list[i])
        end_time = n_list[i][1] #여기서 업데이트

print(len(selected))
