from collections import Counter

a = list(map(int, open(0).read().split()))

#Equilateral
if a.count(60) == 3:
    print("Equilateral")
#Isosceles
elif sum(a)==180 and (2 in Counter(a).values()):
    print("Isosceles")
#Scalene
elif sum(a)==180 and (2 not in Counter(a).values()):
    print("Scalene")
#Error
else:
    print("Error")