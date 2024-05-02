N, M = map(int, input().split())

A = [[0] * N for _ in range(N)]

for _ in range(M):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  A[a][b] = 1
  A[b][a] = 1

for i in range(N):
  for j in range(i+1, N):
    if not A[i][j]:
      print('No')
      exit(0)

print("Yes")