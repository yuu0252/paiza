H, W, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

ans = [[0] * (W+1) for _ in range(H+1)]

for y in range(H):
  for x in  range(W):
    ans[y+1][x+1] = ans[y+1][x] + ans[y][x+1] - ans[y][x] + A[y][x]

for _ in range(N):
  y, x = map(int, input().split())
  print(ans[y][x])