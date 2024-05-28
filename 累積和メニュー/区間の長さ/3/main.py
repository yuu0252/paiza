k = int(input())
A = list(map(int, input().split()))

right = 0
max_section = 0
element_sum = 0

for left in range(10):
  while right < 10:
    if element_sum + A[right] <= k:
      element_sum += A[right]
      right += 1
    else:
      break
  
  max_section = max(max_section, right - left)

  if left == right:
    right += 1
  else:
    element_sum -= A[left]

print(max_section)