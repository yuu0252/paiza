L = [(1, 1), (2, 2), (3, 3), (1, 3), (3, 1)]
R = [(3, 3), (4, 4), (5, 5), (3, 5), (5, 3)]

A = [[0] * (6) for _ in range(6)]

for i in range(5):
  sy, sx = L[i]
  ey, ex = R[i]

  A[sy-1][sx-1] += 1
  A[ey][ex] += 1
  A[sy-1][ex] -= 1
  A[ey][sx-1] -= 1

for i in range(6):
  for j in range(5):
    A[i][j+1] += A[i][j]

for i in range(6):
  for j in range(5):
    A[j+1][i] += A[j][i]

m = 0

for i in range(6):
  for j in range(6):
    m = max(m, A[i][j])

print(m)