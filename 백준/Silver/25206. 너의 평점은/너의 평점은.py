import sys
grade = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0,
         "C+":2.5, "C0":2.0, "D+": 1.5, "D0": 1.0,
         "F":0.0, "P":0.0}
result = 0
credit = 0

for i in sys.stdin.readlines():
    answer = i.strip().split(" ")
    if answer[2] == "P":
        pass
    else:
        result += float(answer[1])*grade[answer[2]]
        credit += float(answer[1])

print(result/credit)