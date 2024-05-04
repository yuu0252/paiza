N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
sums = [0] * (N+1)
for i in range(N):
  sums[i+1] = sums[i] + A[i]

print(sums[Y+1] - sums[X])