H, W, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

total = [[0] * (W+1) for _ in range(H+1)]

for y in range(H):
  for x in range(W):
    total[y+1][x+1] = total[y][x+1] + total[y+1][x] - total[y][x] + A[y][x]

for _ in range(N):
  a, b, c, d = map(int, input().split())
  print(total[c][d] - total[c][b-1] - total[a-1][d] + total[a-1][b-1])
  