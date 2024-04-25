import re

def solution(files):
    def sort_key(file):
        match = re.match(r"([a-z\- .]+)(\d+)", file.lower())
        head = match.group(1) #문자 추출 ([a-z\- .]+)
        number = int(match.group(2)) #숫자 추출 (\d+)
        # print(f'head:{head}, number:{number}')
        return (head, number)
    
    sorted_files = sorted(files, key=sort_key)
    return sorted_files
