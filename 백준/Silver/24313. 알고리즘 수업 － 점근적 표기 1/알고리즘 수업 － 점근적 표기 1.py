a,b,c,d = list(map(int,open(0).read().split()))
print(1 if a*d+b<=c*d and c>=a else 0)