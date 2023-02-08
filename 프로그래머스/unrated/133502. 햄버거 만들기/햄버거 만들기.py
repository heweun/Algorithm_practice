def solution(ingredient):
    answer = 0
    a = [] # 일단 숫자 넣어보고 넣은 숫자로 부터 꺼꾸로 4자리 읽었을 때 확인하기 위함.
    for i in ingredient: # 숫자 하나씩 보자(앞에서 부터)
        a.append(i) # 일단 넣어
        if i == 1 and a[-4:] == [1,2,3,1]: 
			   # 지금 현재 숫자가 1이고(i == 1), a에 넣은 숫자 꺼꾸로 봤을 때(a[-4:]) 1231이야?
            answer += 1 # 개수 세
            for x in range(len(a)-1,len(a)-5,-1): # 개수센거만 지워봐(뒤에서 4자리 숫자만 지워봐 뒤에서 부터 하나씩)
                del a[x]
						# 이거 거치고 나면 뒤에서 1231 이 없어지고 앞에 두개 수 만 남음.
        
    return answer