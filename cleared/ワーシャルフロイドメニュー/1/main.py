n, m = map(int, input().split())
A = [[999] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    A[a-1][b-1] = c

for i in range(n):
    A[i][i] = 0
    print(*A[i])