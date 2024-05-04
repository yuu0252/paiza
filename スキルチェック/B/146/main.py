from collections import deque

A, B = map(int, input().split())
N = int(input())
h = list(map(int, input().split()))

q = deque()
q.append((h, 0))

m = 10 ** 10

while q:
    now, n = q.popleft()
    now.sort(reverse=True)
    
    if now[0] == 0:
        if m > n:
            m = n
        break
    
    q.append(([max(0, now[0] -  A)] + now[1:N], n+1))
    
    for i in range(N):
        if now[i] == 0:
            break
        now[i] = max(0, now[i]-B)
    
    q.append((now, n+1))
    
print(m)
        