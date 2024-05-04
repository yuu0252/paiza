N = int(input())
A = [0] * 11

for _ in range(N):
  l, r = map(int, input().split())
  A[l-1] += 1
  A[r] -= 1

for i in range(N):
  A[i+1] += A[i]

print(max(A))