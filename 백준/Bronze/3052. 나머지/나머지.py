import sys

num_list = [num%42 for num in map(int, sys.stdin.readlines())]
print(len(set(num_list)))