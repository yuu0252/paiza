a = [0] * 11
L = [1, 1, 3, 3, 7]
R = [3, 8, 8, 6, 9]

for i in range(5):
  a[L[i] - 1] += 1
  a[R[i]] -= 1

for i in range(10):
  a[i+1] += a[i]

print(max(a))