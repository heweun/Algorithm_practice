a = list(map(int,open(0).read().split()))
triangle_list = ["Equilateral","Isosceles","Scalene"]

n = 3
set_list = [sorted(a[i:i+n]) for i in range(0,len(a),n)]

for s in set_list:
    if s[0]==0: break

    if sum(s[:-1])<=s[-1]:
        print("Invalid")
    else:
        print(triangle_list[len(set(s))-1])
