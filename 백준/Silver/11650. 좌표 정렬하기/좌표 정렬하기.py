N, *numbers = map(int, open(0).read().split())

array = [[x,y] for x,y in zip(numbers[::2],numbers[1::2])]
array = sorted(array, key = lambda x:(x[0],x[1]))

for i in range(N):
    print(array[i][0],array[i][1])