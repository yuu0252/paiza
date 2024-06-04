n, m, x, y = map(int, input().split())
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

if A[x-1][y-1] == 999:
  print(999)
else:
  prev = y
  path = [y]
  while True:
    prev = B[x-1][prev-1]
    path.append(prev)
    if prev == x:
      break
  print(A[x-1][y-1])
  print(*path[::-1])
  