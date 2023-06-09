N, *people = open(0).read().split()
dic = {}

for i,j in zip(people[::2],people[1::2]): dic[i] = j

print(*sorted([name for name,state in dic.items() if state=='enter'],
              reverse=True), sep = '\n')