N, Q = map(int, input().split())
A = [0] * (N+1)

for _ in range(Q):
  l, r = map(int, input().split())
  A[l-1] += 1
  A[r] -= 1

for i in range(N):
  A[i+1] += A[i]

print(max(A))