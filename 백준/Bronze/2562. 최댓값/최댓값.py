import sys

num_list = list(map(int, sys.stdin.readlines()))
print(max(num_list), num_list.index(max(num_list))+1, sep="\n")