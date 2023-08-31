N = int(input())

def hanoi(num, start, sub, target):
    if num == 0: return
    hanoi(num-1, start, target, sub)
    print(start, sub)
    hanoi(num-1, target, sub, start)
   
print(2**N-1)
hanoi(N,1,3,2)