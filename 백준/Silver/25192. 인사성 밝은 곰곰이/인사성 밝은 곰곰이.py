N = open(0).read().split('ENTER')
#print(N)

answer = 0
for n in N:
    #print(n.split())
    answer += len(set(n.split()))
print(answer-1)