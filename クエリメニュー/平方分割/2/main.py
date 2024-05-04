N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
ans = [0] * (N+1)

for i in range(N):
  ans[i+1] = ans[i] + A[i]

for _ in range(K):
  l, r = map(int, input().split())
  print(ans[r]-ans[l-1])