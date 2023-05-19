N, *number = map(int, open(0).read().split())
print(*sorted(number), sep = '\n')