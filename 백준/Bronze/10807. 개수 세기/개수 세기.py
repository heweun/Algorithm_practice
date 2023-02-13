import sys
input=sys.stdin.readline

num = int(input())
num_list = list(map(int, input().split()))
cnt = int(input())

print(num_list.count(cnt))