n = int(input())

for _ in range(n):
  vps = input()
  while "()" in vps:
    vps = vps.replace('()','')
        
  if len(vps) != 0:
    print('NO')
  else:
    print('YES')