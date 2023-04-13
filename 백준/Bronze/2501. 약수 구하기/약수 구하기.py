a, b = map(int, input().split())
yaksu_list = []

for i in range(1,a+1):
  if a%i == 0:
    yaksu_list.append(i)

print(yaksu_list[b-1] if len(yaksu_list)>=b else 0)