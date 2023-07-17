import sys
import re

input = sys.stdin.readline

while True:
    if (a := input().rstrip()) == '.':
        break
    b = re.sub(r'[a-zA-Z\s]', '', a)
    while '()' in b or '[]' in b:
        b = b.replace('()', '')
        b = b.replace('[]', '')
    if b == '.':
        print('yes')
    else:
        print('no')