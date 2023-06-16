boggy = input()

answer = set()
num = len(boggy)

for i in range(num):
    for j in range(i,num):
        answer.add(boggy[i:j+1])

print(len(answer))