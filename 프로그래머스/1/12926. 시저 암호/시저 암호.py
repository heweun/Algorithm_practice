def solution(s, n):
    result = ''
    for char in s:
        if char.isalpha():  # 알파벳인 경우에만 처리
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + n) % 26 + base)
        else:
            result += char  # 알파벳이 아닌 경우 그대로 유지

    return result