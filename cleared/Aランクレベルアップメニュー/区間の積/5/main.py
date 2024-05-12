N, M = map(int, input().split())
A = list(map(int, input().split()))
total = [0] * (N+1)

for _ in range(M):
  l, u, a = map(int, input().split())
  for i in range(l, u+1):
    total[i] += a

for i in range(N):
  print(A[i] + total[i+1])