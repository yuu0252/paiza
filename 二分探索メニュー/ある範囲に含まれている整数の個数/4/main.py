n = int(input())
A = list(map(int, input().split()))
q = int(input())
A.sort()

def lower_bound(A, k):
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
  l, r = map(int, input().split())
  
  print(lower_bound(A, r) - lower_bound(A, l))