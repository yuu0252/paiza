n, m, x, y  =map(int, input().split())
A = [[999] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    A[a-1][b-1] = c

for i in range(n):
    A[i][i] = 0

m = 999
ans = []

for k in range(1, n+1):
    if k != x and k != y:
        length = A[x-1][k-1] + A[k-1][y-1]
        if length < m:
            m = length
            ans = [k]
        elif length == m:
            ans.append(k)

if m == 999:
    print(m)
    exit()

print(*sorted(ans))