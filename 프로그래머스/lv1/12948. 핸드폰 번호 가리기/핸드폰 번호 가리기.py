import re

def solution(phone_number):
    answer = re.sub("[0-9]","*", phone_number[:-4])+phone_number[-4:]
    return answer