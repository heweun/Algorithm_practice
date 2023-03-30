a = list(map(int,open(0).read().split()))
want = a.index(max(a))

print(max(a))
print(want//9+1, want%9+1)