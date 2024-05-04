A = list(map(int, input().split()))
N = len(A)

sums = [0] * (N+1)

for i in range(N):
  sums[i+1] = sums[i] + A[i]

print(sums[7]-sums[1])