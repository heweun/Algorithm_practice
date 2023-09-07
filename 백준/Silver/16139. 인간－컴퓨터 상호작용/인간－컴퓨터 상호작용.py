import sys

word, _, *n_list = (i.split() for i in sys.stdin.readlines())

word = ''.join(word)
s_word = set(word)  # set으로 중복값 제거

dic = {}  # 딕셔너리 구조로 알파벳 찾기

for alpha in s_word:
    pre = []
    start = 0

    for w in word:
        if w == alpha:
            start += 1
        pre.append(start)

    dic[alpha] = pre

# 만들어둔 딕셔너리에서 검색하기
for n in n_list:
    if n[0] not in dic:  # 예외 처리: 문자에 없던 알파벳이 나옴
        print(0)
    else:
        n[1], n[2] = int(n[1]), int(n[2])  # 문자열을 정수로 변환
        if n[1] == 0:
            print(dic[n[0]][n[2]])
        else:
            print(dic[n[0]][n[2]] - dic[n[0]][n[1] - 1])
