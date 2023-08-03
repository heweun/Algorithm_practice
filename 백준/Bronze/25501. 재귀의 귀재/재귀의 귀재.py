def recursion(s, l, r):
    global cnt; cnt += 1

    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l + 1, r - 1)

def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)

N,*P_list = open(0).read().split()

for p in P_list:
    cnt = 0
    print(isPalindrome(p),cnt)
