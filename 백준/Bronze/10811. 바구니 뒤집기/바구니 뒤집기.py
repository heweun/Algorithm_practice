M, N = map(int, input().split())
m_list = [m for m in range(1,M+1)]

for n in range(N):
  i, j = map(int, input().split())
  m_list[i-1:j] = m_list[i-1:j][::-1]

print(*m_list)