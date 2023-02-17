import sys

num_list = list(map(int, sys.stdin.readlines()))

for i in range(1,31):
    if i not in num_list:
        print(i, sep='/n')