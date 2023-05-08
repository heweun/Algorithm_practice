num = int(input())
print(sum((n**2+n)//2 for n in range(1,num-1)),3,sep = '\n')