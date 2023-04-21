a = list(map(int,open(0).read().split()))

x_list = [i for i in a[0::2]]
y_list = [i for i in a[1::2]]

#x = y = 0
for p in range(3):
  if x_list.count(x_list[p]) == 1:
    x = x_list[p]
  if y_list.count(y_list[p]) == 1:
    y = y_list[p]

print(x,y)
