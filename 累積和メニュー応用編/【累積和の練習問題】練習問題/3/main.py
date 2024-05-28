n, x, y, c = input().split()

n = int(n)
x = int(x)
y = int(y)

s = list(input())

l = [0] * (n+1)

for i in range(n):
  count = 0
  if s[i] == c:
    count += 1
  l[i+1] = l[i] + count

print(l[y] - l[x - 1])