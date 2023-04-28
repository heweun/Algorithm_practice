a_list = sorted(list(map(int, input().split())),reverse=True)

if a_list[0]>=sum(a_list[1:]):
  a_list[0] = sum(a_list[1:])-1
  print(sum(a_list))
else:
  print(sum(a_list))