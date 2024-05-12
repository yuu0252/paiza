h, w = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(h)]

directions = [1, 2, 1, 0, 3]
total = 0

y, x = (0, 0)

while directions:
  d = directions.pop(0)
  if d == 0:
    y -= 1
  if d == 1:
    x += 1
  if d == 2:
    y += 1
  if d == 3:
    x -= 1
  
  total += grid[y][x]

print(total)