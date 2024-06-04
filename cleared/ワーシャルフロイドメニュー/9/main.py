n, m = map(int, input().split())
A = [[999] * n for _ in range(n)]
B = [[j+1] * n for j in range(n)]

for _ in range(m):
  a, b, c = map(int, input().split())
  A[a-1][b-1] = c

for i in range(n):
  A[i][i] = 0

for transit in range(n):
  for start in range(n):
    for goal in range(n):
      if A[start][goal] > A[start][transit] + A[transit][goal]:
        A[start][goal] = A[start][transit] + A[transit][goal]
        B[start][goal] = B[transit][goal]

max_time = 0

for i in range(n):
  for j in range(n):
    if A[i][j] > max_time and A[i][j] < 999:
      max_time = A[i][j]
      s, g = i + 1, j + 1
print(max_time)

path = [g]
prev = g
while True:
  prev = B[s-1][prev-1]
  path.append(prev)
  if prev == s:
    break
print(*path[::-1])