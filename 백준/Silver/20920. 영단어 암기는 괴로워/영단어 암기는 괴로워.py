#0. 길이가 M이상인 단어만
#1. 자주 나오는 단어 앞에 배치
#2. 길이가 길수록 앞에 배치
#3. 사전순으로 앞에 배치
from collections import Counter

N,M,*word = open(0).read().split()

more_M = list(filter(lambda x:len(x)>=int(M),word))
answer = sorted(Counter(more_M).items(), key = lambda x:(-x[1],-len(x[0]),x[0]))
answer = list(map(lambda x:x[0],answer))
print(*answer, sep='\n')