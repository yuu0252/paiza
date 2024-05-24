n, m = map(int, input().split())

A = [[999] * n for _ in range(n)]

for i in range(m):
  a, b = map(int, input().split())
  A[a-1][b-1] = 1

for i in range(n):
  A[i][i] = 0


for transit in range(n):
  for start in range(n):
    for goal in range(n):
      A[start][goal] = min(
        A[start][goal], A[start][transit] + A[transit][goal]
      )

for i in range(n):
  for j in range(n):
    if A[i][j] == 999:
      print("No")
      exit()

print("Yes")