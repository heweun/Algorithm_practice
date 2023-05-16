N,M,*a_list = open(0).read().split()
result = []

#리스트를 8*8로 쪼개기
for i in range(int(N)-7): #N을 넘지 않는 수 중 가장 큰 수 까지
    for j in range(int(M)-7): #M을 넘지 않는 수 중 가장 큰 수 까지
        count1 = 0
        count2 = 0

#쪼갠 8*8 검사하기
        for x in range(i,i+8):
            for y in range(j,j+8):
                #인덱스의 합이 짝수->시작점과 같아야함
                if (x+y)%2 == 0:
                    if a_list[x][y]!= 'W': #W가 아니면
                        count1 += 1 #W로 바꿔주고 +1
                    else: #반대의 경우
                        count2 += 1 #B로 바꿔주고 +1
                #인덱스의 합이 홀수->시작점과 달라야함
                else:
                    if a_list[x][y] != 'W': #W가 아니면
                        count2 += 1 #B로 바꿔주고 +1
                    else: #B가 아니면
                        count1 += 1 #W로 바꿔주고 +1
        result.append(count1) #W로 시작할때 경우의 수
        result.append(count2) #B로 시작할때 경우의 수
print(min(result))