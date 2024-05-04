s = "1 5 9 7 5 3 2 5 8 4"
A = list(map(int, s.split()))
N = len(A)

sums = [0] * (N+1)

for i in range(N):
  sums[i+1] = sums[i] + A[i]

print(sums[7] - sums[1])