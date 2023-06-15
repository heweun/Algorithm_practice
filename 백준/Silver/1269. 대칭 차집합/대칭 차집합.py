_,A,B = open(0)

join = set(A.split())|set(B.split())
inner = set(A.split())&set(B.split())
print(len(join)-len(inner))