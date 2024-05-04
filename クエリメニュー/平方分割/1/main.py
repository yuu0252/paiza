N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

total = [0] * (N+1)

for i in range(N):
  total[i+1] = total[i] + A[i]

for _ in range(K):
  q = int(input())
  print(total[q])