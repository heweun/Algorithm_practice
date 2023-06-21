x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())

bunza = x1*y2 + x2*y1
bunmo = y1*y2

x = bunza
y = bunmo
while y:
    #print("x:",x, "y:",y)
    if x > y:
        x,y = y,x%y
    else:
        y %= x

print(bunza//x, bunmo//x)