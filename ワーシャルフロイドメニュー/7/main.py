n, m, x, y = map(int, input().split())
A = [[999] * n for _ in range(n)]

for _ in range(m):
  a, b, c = map(int, input().split())
  A[a-1][b-1] = c

for i in range(n):
  A[i][i] = 0

for transit in range(n):
  for start in range(n):
    for goal in range(n):
      A[start][goal] = min(
        A[start][goal], A[start][transit] + A[transit][goal]
      )

for i in range(n):
  if A[i][i] < 0:
    print("Inf")
    exit()

print(A[x-1][y-1])