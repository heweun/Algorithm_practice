N, *basic = map(int, open(0).read().split())

first = 1
spare = []

while basic:
  if first == basic[0]:
    first +=1
    basic.pop(0)
  else:
    spare.append(basic.pop(0))

  
  while spare:
    if spare[-1] == first:
      spare.pop()
      first += 1
    
    else:
      break

print('Sad') if spare else print('Nice')