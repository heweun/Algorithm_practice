p = [0 for i in range(101)]
p[1] = 1; p[2] = 1; p[3] = 1
#print(f'p:{p}')

for i in range(4,101):
  p[i] = p[i-3]+p[i-2]

_, *n_list = map(int, open(0).read().split())

for n in n_list:
  print(p[n])