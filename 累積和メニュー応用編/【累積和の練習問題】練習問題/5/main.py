n, a, b = map(int, input().split())
s = list(input())

b = [0] * n

s = [0] * (n + 1)

for i in range(n-2):
    if s[i:i+3] == "piz":
        b[i] = 1

for i in range(n):
    s[i + 1] = s[i] + b[i]

print(s[b - 2] - s[a - 1])