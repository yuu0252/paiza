n, s, k = map(int, input().split())

import random

edges = []
trail = [s]

for i in range(k):
    ng_neighbors = set()
    while True:
        next_s = random.choice(list(set(range(1, n+1)) - {s} - ng_neighbors))
        e = tuple(sorted((s, next_s)))
        if e not in edges:
            break
        ng_neighbors.add(next_s)
    trail.append(next_s)
    edges.append(e)
    s = next_s

print(*trail)