n,n_list,_,check_list = ([*map(int,i.split())] for i in open(0))
#print(f'n:{n},n_list:{n_list},check_list:{check_list}')
n = n[0]
n_list.sort(key = lambda x:x)

#n_list: 정렬된 리스트/ taget: 찾으려는 값/ start:범위의 시작/ end:범위의 끝
def binary_check(n_list, target, start, end):
  if start>end: return 0 #정 없으면 0출력하도록
  mid = (start+end)//2 #중간으로 나눌 기준값

  #target == mid / target< mid / target>mid 로 나눠서 보기
  if n_list[mid] == target:
    return 1
  elif n_list[mid] > target:
    return binary_check(n_list, target, start, mid-1)
  else:
    return binary_check(n_list, target, mid+1, end)

for t in check_list:
  #print(f't:{t}')
  print(binary_check(n_list,t,0,n-1))