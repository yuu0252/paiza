n = int(input())
A = list(map(int, input().split()))

l = [0] * (n + 1)
L = [0] * (n + 1)

for i in range(n):
    l[i + 1] = l[i] + A[i]

for i in range(n):
    L[i + 1] = L[i] + l[i + 1]


print(max(L))