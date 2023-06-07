N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

dic = {}

for m in M_list:
  dic[m]=0

for n in N_list:
  if n in dic:
    dic[n]=1
    
for d in dic:
  print(dic[d], end = ' ')