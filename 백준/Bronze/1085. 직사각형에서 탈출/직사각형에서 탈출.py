x,y,w,h = map(int, input().split())

compare_list = [abs(0-x),abs(0-y),w-x,h-y]
print(min(compare_list))