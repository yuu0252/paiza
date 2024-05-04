A = [0] * 11

for _ in range(5):
  l, r = map(int, input().split())
  A[l-1] += 1
  A[r] -= 1

for i in range(10):
  A[i+1] += A[i]

print(max(A))