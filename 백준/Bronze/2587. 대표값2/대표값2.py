num = list(map(int, open(0).read().split()))
print(sum(num)//5, sorted(num)[2], sep = '\n')