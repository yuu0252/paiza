n = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
q = int(input())

def lower_bound(A, n, k):
  left = 0
  right = n


  while left < right:
    mid = (left + right) // 2
    if A[mid] < k:
      left = mid + 1
    else:
      right = mid

  return left

for _ in range(q):
  k = int(input())
  print(lower_bound(A, n, k))