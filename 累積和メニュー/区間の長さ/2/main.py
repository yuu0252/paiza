A = list(map(int, input().split()))
max_section = 0
right = 0
element_sum = 0

for left in range(10):
  while right < 10:
    if element_sum + A[right] <= 15:
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