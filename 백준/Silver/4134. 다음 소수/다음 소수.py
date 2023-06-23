from math import sqrt
a,*n_list = map(int, open(0).read().split())

def check(N):
    if N==0 or N==1:
        return False
    for n in range(2,int(sqrt(N))+1):
        if N%n == 0:
            return False
    return True

for i in n_list:
    while True:
        if check(i):
            print(i)
            break
        else:
            i += 1