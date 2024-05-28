n, k = map(int, input().split())
A = list(map(int, input().split()))

max_section = 0
l = [0] * (n+1)

for i in range(n):
  l[i+1] = l[i] + A[i]

for i in range(n - k + 1):
  max_section = max(max_section, l[i + k] - l[i])

print(max_section)