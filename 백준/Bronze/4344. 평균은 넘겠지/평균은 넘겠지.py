num = int(input())

for _ in range(num):
  num_list = list(map(int, input().split()))
  answer = 0
  for i in num_list[1:]:
    if i>sum(num_list[1:])/num_list[0]:
      answer += 1
  print("{:.3f}%".format(answer/num_list[0]*100))