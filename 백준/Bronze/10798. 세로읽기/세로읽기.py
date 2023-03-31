a = open(0).read().split()

for i in range(max(len(i) for i in a)):
    for j in range(5):
        try:
            print(a[j][i], end='')
        except:
            pass