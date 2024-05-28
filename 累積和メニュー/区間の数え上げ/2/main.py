A = list(map(int, input().split()))

section_count = 0
element_sum = 0
right = 0

for left in range(10):
  while right < 10:
    if element_sum + A[right] <= 15:
      element_sum += A[right]
      right += 1
    else:
      break
  
  section_count += right - left
  
  if left == right:
    right += 1
  else:
    element_sum -= A[left]

print(section_count)