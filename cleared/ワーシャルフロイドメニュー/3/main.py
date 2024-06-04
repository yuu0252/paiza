n, m, q = map(int, input().split())
A = [[999] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    A[a-1][b-1] = c

for i in range(n):
    A[i][i] = 0


for _ in range(q):
    d, e, f = map(int, input().split())
    if A[d-1][f-1] < min(A[d-1][e-1] + A[e-1][f-1], 999):
        print("direct")
    elif A[d-1][f-1] == min(A[d-1][e-1] + A[e-1][f-1], 999):
        print("same")
    else:
        print("transit")